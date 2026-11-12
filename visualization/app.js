'use strict';

// Catalog, DOM references, and viewer state
const catalog = JSON.parse(document.getElementById('catalog-data').textContent);
const all = new Map(catalog['@graph'].map(n => [n.id, n]));
const concepts = catalog['@graph'].filter(n => n.type === 'Concept');
const ids = new Set(concepts.map(n => n.id));
const categories = catalog['@graph'].filter(n => n.type === 'Category');
const palette = ['#bca5f7', '#f1c670', '#8dc9fb', '#6ed7b6', '#f3a3c3', '#eda983', '#8fb6ff', '#bacb79', '#c89dcb', '#82d2cf', '#e38f87'];
const colors = new Map(categories.map((c, i) => [c.id, palette[i % palette.length]]));
const relNames = {
  requiresConcept: 'requires',
  specializationOf: 'specializes',
  relatedConcept: 'related to'
};
const edges = concepts.flatMap(n => Object.keys(relNames).flatMap(type => (n[type] || []).filter(id => ids.has(id) && id !== n.id).map(target => ({
  source: n.id,
  target,
  type
}))));

// DOM references and subjects
const $ = id => document.getElementById(id);
const ns = 'http://www.w3.org/2000/svg';
const categoryById = new Map(categories.map(c => [c.id, c]));
const subjectChildren = new Map(categories.map(c => [c.id, categories.filter(child => child.parentCategory === c.id)]));
const subjectRoots = categories.filter(c => !c.parentCategory);
const subjectDepth = Math.max(0, ...categories.map(c => categoryPath(c.id).length - 1));

// Selection state
let pinned = null;
let preview = null;
let category = null;
let view = 'subject';
const viewDescriptions = {
  subject: 'Subjects group concepts for browsing; membership does not imply mathematical inheritance.',
  specialization: 'General concepts appear above their specializations. Arrows point from a specialization to its recorded parent; axioms are not inherited.',
  dependency: 'Prerequisites appear above the concepts that require them. Cyclic prerequisite groups share a level; prerequisites do not imply specialization.'
};

// Cached graph geometry
const positions = new Map();
const nodeEls = new Map();
const edgeEls = [];
const parents = new Map(concepts.map(n => [n.id, (n.specializationOf || []).filter(id => ids.has(id))]));
const children = new Map(concepts.map(n => [n.id, concepts.filter(c => parents.get(c.id).includes(n.id)).map(c => c.id)]));
let shown = new Set();
let overviewSpan = 1500;

// Label measurement cache
let labelPlan = null;
const labelMeasurements = new WeakMap();
const labelCanvas = document.createElement('canvas');
const labelContext = labelCanvas.getContext('2d');

// SVG layers
const edgeDefs = $('edge-defs');
const scene = $('scene');
const membership = el('g');
const edgeGroup = el('g');
const nodeGroup = el('g');
const sectorGroup = el('g');
const groups = categories.map(c => ({
  category: c,
  members: concepts.filter(n => n.category?.[0] === c.id).sort((a, b) => a.fullName.localeCompare(b.fullName))
}));

// Camera and pointer state
let viewCenter = {
  x: 0,
  y: 0
};
let viewSpan = 1500;
let targetView = {
  x: 0,
  y: 0,
  span: 1500
};
let animation = null;
const svg = $('graph');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const graphStage = svg.closest('.stage');
let graphPointerInside = false;
const zoomStep = 1.25;
const selectionZoomOutSteps = 7;
let drag = null;

// DOM and graph helpers

function el(tag, attrs = {}, text) {
  const n = document.createElementNS(ns, tag);
  Object.entries(attrs).forEach(([k, v]) => n.setAttribute(k, v));
  if (text !== undefined) n.textContent = text;
  return n;
}

function html(tag, text, cls) {
  const n = document.createElement(tag);
  if (text !== undefined) n.textContent = text;
  if (cls) n.className = cls;
  return n;
}

function point(angle, r) {
  return [r * Math.cos(angle), r * Math.sin(angle)];
}

function enabled() {
  return new Set([...$('filters').querySelectorAll('input[value]:checked')].map(n => n.value));
}

function visibleEdges() {
  const types = enabled();
  return edges.filter(e => types.has(e.type) && shown.has(e.source) && shown.has(e.target));
}

function categoryPath(id) {
  const path = [];
  while (id) {
    path.unshift(id);
    id = categoryById.get(id)?.parentCategory;
  }
  return path;
}

function inCategory(concept, id) {
  return concept.category.some(c => categoryPath(c).includes(id));
}

// Selection and search

function pick(id) {
  pinned = id;
  preview = null;
  category = null;
  $('concept-select').value = id || '';
  layout();
  update();
  focusSelection();
}

function clear() {
  pinned = preview = category = null;
  $('search').value = '';
  options();
  $('concept-select').value = '';
  layout();
  update();
  fit();
}

function options() {
  const q = $('search').value.toLowerCase().trim();
  const select = $('concept-select');
  select.replaceChildren(new Option('Select a concept', ''));
  concepts.filter(n => (n.shortForm + ' ' + n.fullName).toLowerCase().includes(q)).sort((a, b) => a.fullName.localeCompare(b.fullName)).forEach(n => select.add(new Option(n.fullName, n.id)));
  if (pinned && [...select.options].some(o => o.value === pinned)) select.value = pinned;
}

function showCategory(id) {
  category = id;
  pinned = preview = null;
  $('concept-select').value = '';
  layout();
  update();
  focusSelection();
}

function changeView() {
  view = $('view-mode').value;
  preview = null;
  document.querySelectorAll('#filters input[value]').forEach(input => {
    const allowed = view === 'subject' || input.value === (view === 'specialization' ? 'specializationOf' : 'requiresConcept');
    input.disabled = !allowed;
    input.checked = allowed;
  });
  layout();
  update();
  focusSelection();
}

// Label geometry

// label-geometry:start
function wrapLabel(value, maxWidth, measure) {
  const tokens = value.replace(/([a-z0-9])([A-Z])/g, '$1\u200b$2').split(/\u200b|(?<=\s)/);
  const lines = [];
  let line = '';
  for (const token of tokens) {
    if (line && measure(line + token) > maxWidth) {
      lines.push(line.trimEnd());
      line = '';
    }
    for (const char of token) {
      if (line && measure(line + char) > maxWidth) {
        lines.push(line.trimEnd());
        line = '';
      }
      line += char;
    }
  }
  if (line.trim()) lines.push(line.trimEnd());
  return lines;
}

function labelOverlap(a, b, padding = 3) {
  return a.left < b.right + padding && a.right + padding > b.left && a.top < b.bottom + padding && a.bottom + padding > b.top;
}

function placeLabels(candidates, obstacles = []) {
  const accepted = [];
  for (const candidate of [...candidates].sort((a, b) => b.priority - a.priority || a.id.localeCompare(b.id))) {
    const placement = candidate.placements.find(({
      rect: r
    }) => !obstacles.some(box => labelOverlap(r, box)) && !accepted.some(other => labelOverlap(r, other.rect)));
    if (placement) accepted.push({
      ...candidate,
      ...placement
    });
  }
  return accepted;
}
// label-geometry:end

// Measured, fixed label rendering

function wrapSvgLabel(text, value, maxWidth) {
  const style = getComputedStyle(text);
  const font = `${style.fontStyle} ${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
  const letterSpacing = parseFloat(style.letterSpacing) || 0;
  const key = JSON.stringify([value, maxWidth, font, letterSpacing, text.getAttribute('x'), text.dataset.centerLine]);
  if (labelMeasurements.get(text) === key) return;
  labelContext.font = font;
  const measure = value => labelContext.measureText(value).width + Math.max(0, value.length - 1) * letterSpacing;
  const lines = wrapLabel(value, maxWidth, measure);
  const lineHeight = parseFloat(style.fontSize) * 1.25;
  const metrics = labelContext.measureText(lines[0] || '');
  const firstDy = text.dataset.centerLine === 'true' ? (metrics.actualBoundingBoxAscent - metrics.actualBoundingBoxDescent) / 2 : -(lines.length - 1) * lineHeight / 2;
  text.replaceChildren();
  lines.forEach((line, i) => text.append(el('tspan', {
    x: text.getAttribute('x'),
    dy: i ? lineHeight : firstDy
  }, line)));
  labelMeasurements.set(text, key);
}

function rememberLabelGeometry() {
  labelPlan = null;
  document.querySelectorAll('#graph .node text,#graph .sector text').forEach(text => text.dataset.baseTransform = text.getAttribute('transform') || '');
}

function showLabelPreview() {
  const tooltip = $('label-preview');
  const matrix = $('graph').getScreenCTM();
  tooltip.hidden = !preview || !matrix || !shown.has(preview);
  if (tooltip.hidden) return;
  tooltip.textContent = all.get(preview).fullName;
  tooltip.style.left = '8px';
  tooltip.style.top = '8px';
  const at = positions.get(preview);
  const point = new DOMPoint(at.x, at.y).matrixTransform(matrix);
  const bounds = $('graph').parentElement.getBoundingClientRect();
  tooltip.style.left = Math.max(8, Math.min(bounds.width - tooltip.offsetWidth - 8, point.x - bounds.left + 14)) + 'px';
  tooltip.style.top = Math.max(8, Math.min(bounds.height - tooltip.offsetHeight - 8, point.y - bounds.top + 14)) + 'px';
}

function labelTransformMatrix(text) {
  let matrix = new DOMMatrix();
  for (let i = 0; i < text.transform.baseVal.numberOfItems; i++) matrix = matrix.multiply(text.transform.baseVal.getItem(i).matrix);
  return matrix;
}

function worldLabelRect(text) {
  const style = getComputedStyle(text);
  const size = parseFloat(style.fontSize);
  const spacing = parseFloat(style.letterSpacing) || 0;
  labelContext.font = `${style.fontStyle} ${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
  const spans = [...text.querySelectorAll('tspan')];
  const lines = spans.length ? spans.map(t => t.textContent) : [text.textContent];
  const width = Math.max(0, ...lines.map(line => labelContext.measureText(line).width + Math.max(0, line.length - 1) * spacing));
  const x = Number(text.getAttribute('x'));
  const y = Number(text.getAttribute('y')) + (parseFloat(text.getAttribute('dy')) || 0) + (spans.length ? Number(spans[0].getAttribute('dy')) : 0);
  const anchor = text.getAttribute('text-anchor');
  const left = x - (anchor === 'middle' ? width / 2 : anchor === 'end' ? width : 0);
  const top = y - size;
  const bottom = y + (lines.length - 1) * size * 1.25 + size * .35;
  const matrix = labelTransformMatrix(text);
  const corners = [[left - 2, top], [left + width + 2, top], [left - 2, bottom], [left + width + 2, bottom]].map(([x, y]) => new DOMPoint(x, y).matrixTransform(matrix));
  return {
    left: Math.min(...corners.map(p => p.x)),
    right: Math.max(...corners.map(p => p.x)),
    top: Math.min(...corners.map(p => p.y)),
    bottom: Math.max(...corners.map(p => p.y))
  };
}

function refreshLabels() {
  if (!labelPlan) {
    const candidates = [];
    function candidate(text, value, width, id, priority, fixed = false) {
      const base = text.dataset.baseTransform || '';
      text.setAttribute('transform', base);
      wrapSvgLabel(text, value, width);
      const r = worldLabelRect(text);
      const placements = (fixed ? [[0, 0]] : [[0, 0], [0, -18], [0, 18], [18, 0], [-18, 0], [0, -36], [0, 36]]).map(([dx, dy]) => ({
        dx,
        dy,
        rect: {
          left: r.left + dx,
          right: r.right + dx,
          top: r.top + dy,
          bottom: r.bottom + dy
        }
      }));
      candidates.push({
        text,
        id,
        priority,
        placements,
        base
      });
    }
    nodeEls.forEach((group, id) => {
      if (shown.has(id)) candidate(group.querySelector('text'), all.get(id).shortForm, 180, id, 200);
    });
    sectorGroup.querySelectorAll('.sector').forEach(group => {
      const text = group.querySelector('text');
      const id = group.dataset.category;
      const subject = all.get(id);
      const width = subject.parentCategory ? Infinity : Number(text.dataset.wrapWidth) || 180;
      candidate(text, subject.label, width, id, 150 - Number(group.dataset.depth || 0) * 10, !!subject.parentCategory);
    });
    const obstacles = [...$('graph').querySelectorAll('.center-title')].map(worldLabelRect);
    const accepted = new Map(placeLabels(candidates, obstacles).map(label => [label.id, label]));
    labelPlan = candidates.map(label => ({
      id: label.id,
      text: label.text,
      base: label.base,
      placement: accepted.get(label.id) || label.placements[0]
    }));
    for (const label of labelPlan) {
      label.text.style.visibility = 'visible';
      label.text.setAttribute('transform', `translate(${label.placement.dx} ${label.placement.dy}) ${label.base}`.trim());
    }
  }
  for (const label of labelPlan) {
    const node = all.get(label.id);
    const visible = node.type !== 'Category' || !node.parentCategory || node.id === category;
    label.text.style.visibility = visible ? 'visible' : 'hidden';
  }
  showLabelPreview();
}

// Relationship graph ranks (cycles share a level)

// layout-ranks:start
function relationLayers(nodes, links) {
  const adjacency = new Map(nodes.map(id => [id, []]));
  links.forEach(e => {
    if (adjacency.has(e.source) && adjacency.has(e.target)) adjacency.get(e.source).push(e.target);
  });
  let next = 0;
  const indices = new Map();
  const low = new Map();
  const stack = [];
  const onStack = new Set();
  const components = [];
  function visit(id) {
    indices.set(id, next);
    low.set(id, next++);
    stack.push(id);
    onStack.add(id);
    adjacency.get(id).forEach(target => {
      if (!indices.has(target)) {
        visit(target);
        low.set(id, Math.min(low.get(id), low.get(target)));
      } else if (onStack.has(target)) low.set(id, Math.min(low.get(id), indices.get(target)));
    });
    if (low.get(id) === indices.get(id)) {
      const component = [];
      let member;
      do {
        member = stack.pop();
        onStack.delete(member);
        component.push(member);
      } while (member !== id);
      components.push(component);
    }
  }
  nodes.forEach(id => {
    if (!indices.has(id)) visit(id);
  });
  const owner = new Map();
  components.forEach((members, i) => members.forEach(id => owner.set(id, i)));
  const upstream = components.map(() => new Set());
  links.forEach(e => {
    const a = owner.get(e.source);
    const b = owner.get(e.target);
    if (a !== undefined && b !== undefined && a !== b) upstream[a].add(b);
  });
  const ranks = new Map();
  function rank(i) {
    if (!ranks.has(i)) ranks.set(i, Math.max(-1, ...[...upstream[i]].map(rank)) + 1);
    return ranks.get(i);
  }
  return new Map(nodes.map(id => [id, rank(owner.get(id))]));
}
// layout-ranks:end

// Subject and relationship layouts

function layoutRelations() {
  const type = view === 'specialization' ? 'specializationOf' : 'requiresConcept';
  const ranks = relationLayers(concepts.map(n => n.id), edges.filter(e => e.type === type));
  const levels = new Map();
  concepts.forEach(n => {
    const rank = ranks.get(n.id);
    if (!levels.has(rank)) levels.set(rank, []);
    levels.get(rank).push(n);
  });
  const columns = 8;
  const columnWidth = 245;
  const rowHeight = 70;
  let top = 0;
  [...levels.entries()].sort((a, b) => a[0] - b[0]).forEach(([rank, members]) => {
    members.sort((a, b) => ((all.get((a[type] || [])[0])?.fullName || '') + a.fullName).localeCompare((all.get((b[type] || [])[0])?.fullName || '') + b.fullName));
    sectorGroup.append(el('text', {
      x: -columns * columnWidth / 2,
      y: top - 30,
      class: 'center-title'
    }, `${view === 'specialization' ? 'SPECIALIZATION' : 'PREREQUISITE'} LEVEL ${rank}`));
    members.forEach((n, i) => {
      const x = (i % columns - columns / 2) * columnWidth;
      const y = top + Math.floor(i / columns) * rowHeight;
      positions.set(n.id, {
        x,
        y,
        a: 0
      });
    });
    top += Math.ceil(members.length / columns) * rowHeight + 85;
  });
  overviewSpan = Math.max(columns * columnWidth + 380, top + 150);
  nodeEls.forEach((group, id) => {
    const {
      x,
      y
    } = positions.get(id);
    const circle = group.querySelector('circle');
    const text = group.querySelector('text');
    group.style.display = '';
    group.setAttribute('tabindex', '0');
    circle.setAttribute('cx', x);
    circle.setAttribute('cy', y);
    Object.entries({
      x: x + 12,
      y,
      'text-anchor': 'start',
      transform: ''
    }).forEach(([k, v]) => text.setAttribute(k, v));
  });
  edgeEls.forEach(({
    edge: e,
    element,
    gradient
  }) => {
    const a = positions.get(e.source);
    const b = positions.get(e.target);
    const dx = b.x - a.x;
    const dy = b.y - a.y;
    const len = Math.hypot(dx, dy) || 1;
    const x = b.x - dx / len * 9;
    const y = b.y - dy / len * 9;
    const bend = (a.y + b.y) / 2;
    element.setAttribute('d', `M${a.x},${a.y} C${a.x},${bend} ${x},${bend} ${x},${y}`);
    Object.entries({
      x1: a.x,
      y1: a.y,
      x2: x,
      y2: y
    }).forEach(([k, v]) => gradient.setAttribute(k, v));
  });
}

function layout() {
  shown = new Set(ids);
  membership.replaceChildren();
  sectorGroup.replaceChildren();
  if (view !== 'subject') {
    layoutRelations();
    rememberLabelGeometry();
    return;
  }
  const direct = new Map(groups.map(g => [g.category.id, g.members.filter(n => shown.has(n.id))]));
  const count = c => direct.get(c.id).length + subjectChildren.get(c.id).reduce((sum, child) => sum + count(child), 0);
  const roots = subjectRoots.filter(c => count(c));
  const totalWeight = roots.reduce((sum, c) => sum + count(c), 0);
  const gap = .085;
  const usable = Math.PI * 2 - gap * roots.length;
  const radius = Math.max(343, shown.size * 25 / usable);
  const labelExtent = Math.max(0, ...concepts.filter(n => shown.has(n.id)).map(n => n.shortForm.length * 8.8));
  const outer = radius + labelExtent + 52;
  const ringStep = 40;
  overviewSpan = 2 * (outer + subjectDepth * ringStep + 105);
  function drawSubject(c, start, end, depth) {
    const span = end - start;
    const mid = (start + end) / 2;
    const arcRadius = outer + (subjectDepth - depth) * ringStep;
    const stroke = colors.get(c.id);
    const [sx, sy] = point(start, arcRadius);
    const [ex, ey] = point(end, arcRadius);
    const path = categoryPath(c.id).map(id => categoryById.get(id).label).join(' → ');
    const group = el('g', {
      class: 'sector',
      tabindex: '0',
      role: 'button',
      'data-category': c.id,
      'data-depth': depth,
      'aria-pressed': String(category === c.id),
      'aria-label': path + ': ' + count(c) + ' visible concepts'
    });
    group.append(el('title', {}, path));
    group.append(el('path', {
      d: `M${sx},${sy} A${arcRadius},${arcRadius} 0 ${span > Math.PI ? 1 : 0} 1 ${ex},${ey}`,
      stroke
    }));
    const labelRadius = arcRadius + (depth ? ringStep / 2 : 30);
    const [tx, ty] = point(mid, labelRadius);
    let deg = mid * 180 / Math.PI + 90;
    if (deg > 90 && deg < 270) deg += 180;
    const label = el('text', {
      x: tx,
      y: ty,
      'text-anchor': 'middle',
      transform: `rotate(${deg} ${tx} ${ty})`
    });
    if (depth) label.dataset.centerLine = 'true';
    label.dataset.wrapWidth = Math.max(80, Math.min(220, arcRadius * span * .8));
    group.append(label);
    group.addEventListener('focus', refreshLabels);
    group.addEventListener('blur', refreshLabels);
    group.addEventListener('mouseenter', refreshLabels);
    group.addEventListener('mouseleave', refreshLabels);
    group.addEventListener('click', () => showCategory(c.id));
    group.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        showCategory(c.id);
      }
    });
    sectorGroup.append(group);
    const members = direct.get(c.id);
    const unit = span / count(c);
    members.forEach((n, i) => {
      const a = start + unit * (i + .5);
      const [x, y] = point(a, radius);
      positions.set(n.id, {
        x,
        y,
        a
      });
      const [ox, oy] = point(a, arcRadius - 10);
      membership.append(el('line', {
        x1: x,
        y1: y,
        x2: ox,
        y2: oy,
        stroke,
        class: 'membership'
      }));
    });
    let cursor = start + unit * members.length;
    subjectChildren.get(c.id).filter(child => count(child)).forEach(child => {
      const childEnd = cursor + unit * count(child);
      const inset = Math.min(.018, (childEnd - cursor) * .06);
      drawSubject(child, cursor + inset, childEnd - inset, depth + 1);
      cursor = childEnd;
    });
  }
  let offset = -Math.PI / 2;
  roots.forEach(c => {
    const span = usable * count(c) / totalWeight;
    drawSubject(c, offset, offset + span, 0);
    offset += span + gap;
  });
  nodeEls.forEach((group, id) => {
    group.style.display = shown.has(id) ? '' : 'none';
    group.setAttribute('tabindex', shown.has(id) ? '0' : '-1');
    if (!shown.has(id)) return;
    const {
      x,
      y,
      a
    } = positions.get(id);
    const [tx, ty] = point(a, radius + 12);
    const left = Math.cos(a) < 0;
    const circle = group.querySelector('circle');
    const text = group.querySelector('text');
    text.style.display = '';
    circle.setAttribute('cx', x);
    circle.setAttribute('cy', y);
    Object.entries({
      x: tx,
      y: ty,
      'text-anchor': left ? 'end' : 'start',
      transform: `rotate(${a * 180 / Math.PI + (left ? 180 : 0)} ${tx} ${ty})`
    }).forEach(([k, v]) => text.setAttribute(k, v));
  });
  edgeEls.forEach(({
    edge: e,
    element,
    gradient
  }) => {
    if (!shown.has(e.source) || !shown.has(e.target)) return;
    const s = positions.get(e.source);
    const t = positions.get(e.target);
    const len = Math.hypot(t.x - s.x, t.y - s.y) || 1;
    const x = t.x - (t.x - s.x) / len * 8;
    const y = t.y - (t.y - s.y) / len * 8;
    element.setAttribute('d', `M${s.x},${s.y} Q0,0 ${x},${y}`);
    Object.entries({
      x1: s.x,
      y1: s.y,
      x2: x,
      y2: y
    }).forEach(([k, v]) => gradient.setAttribute(k, v));
  });
  rememberLabelGeometry();
}

// Details pane and relationship highlighting

function renderDetails(id, activeEdges) {
  const panel = $('details');
  panel.replaceChildren();
  if (!id) {
    panel.append(html('div', category ? 'SUBJECT AREA' : 'EXPLORE THE CATALOG', 'eyebrow'));
    panel.append(html('div', category ? categoryPath(category).map(id => all.get(id).label).join(' → ') : 'Follow a connection', 'detail-title'));
    panel.append(html('p', category ? 'Highlighted nodes belong to this subject or its subsubjects. Select a node to inspect its relationships and mathematical definition.' : 'Select a concept to see its definition, notation, operations, and governing claims. Hovering previews the same neighborhood.'));
    if (category) {
      concepts.filter(n => inCategory(n, category)).forEach(n => {
        const b = html('button', n.fullName, 'relation-button');
        b.onclick = () => pick(n.id);
        panel.append(b);
      });
    }
    panel.append(html('p', viewDescriptions[view] + ' Select a subject to highlight all its descendant memberships. Search and concept selection remain available in every view.', 'footer'));
    return;
  }
  const n = all.get(id);
  panel.append(html('div', preview ? 'CONCEPT PREVIEW' : 'SELECTED CONCEPT', 'eyebrow'), html('div', n.fullName, 'detail-title'));
  const page = html('a', 'Open Markdown concept page');
  page.href = (location.hostname === 'brteja1.github.io' ? 'https://github.com/brteja1/mathematical-abstractions/blob/main/concepts/' : '../concepts/') + encodeURIComponent(n.shortForm) + '.md';
  panel.append(page);
  n.category.forEach(c => {
    const badge = html('span', categoryPath(c).map(id => all.get(id).label).join(' → '), 'badge');
    badge.style.borderColor = colors.get(c);
    panel.append(badge);
  });
  panel.append(html('span', all.get(n.kind)?.label || n.kind, 'badge'));
  panel.append(html('p', n.definition), html('h2', 'Mathematical definition'), html('div', n.notation, 'notation'));
  if (n.mathematicalFormulation) {
    panel.append(html('h2', 'Mathematical formulation'), html('div', n.mathematicalFormulation, 'notation'));
  }
  if (n.leanFormulation) {
    const formal = html('details');
    formal.append(html('summary', `Lean formulation · ${n.formulationScope}`), html('pre', n.leanFormulation, 'notation'),
      html('p', n.leanModelMapping), html('p', n.leanModelLimitations, 'empty'),
      html('p', 'Read in its source module context. Definitions and structure hypotheses are not proof witnesses. Consult a fresh Lean verification report for compiler and axiom-audit evidence.', 'empty'));
    panel.append(formal);
  }
  if (n.axiomBasis) {
    panel.append(html('h2', 'Mathematical basis'), html('p', n.axiomBasis));
    if (n.basisScope) panel.append(html('p', n.basisScope, 'empty'));
  }
  ['incoming', 'outgoing'].forEach(direction => {
    const list = activeEdges.filter(e => direction === 'incoming' ? e.target === id : e.source === id);
    panel.append(html('h2', `${direction} · ${list.length}`));
    if (!list.length) panel.append(html('p', 'No links of the enabled types are recorded.', 'empty'));
    list.forEach(e => {
      const target = direction === 'incoming' ? e.source : e.target;
      const b = html('button', all.get(target).fullName, 'relation-button');
      b.append(html('small', direction === 'incoming' ? `${relNames[e.type]} this concept` : `This concept ${relNames[e.type]} →`));
      b.onclick = () => pick(target);
      panel.append(b);
    });
  });
  [['hasOperation', 'Operations'], ['hasAxiom', 'Axioms'], ['hasLaw', 'Laws'], ['hasTheorem', 'Theorems']].forEach(([key, label]) => {
    const refs = n[key] || [];
    panel.append(html('h2', `${label} · ${refs.length}`));
    if (!refs.length) panel.append(html('p', 'No entries recorded yet.', 'empty'));
    refs.forEach(ref => {
      const item = all.get(ref);
      if (!item) return;
      const det = html('details');
      const summary = html('summary', item.name || item.statement);
      det.append(summary);
      if (item.signature || item.formalStatement) det.append(html('div', item.signature || item.formalStatement, 'notation'));
      if (item.leanFormulation) {
        det.append(html('h3', 'Lean proposition'), html('pre', item.leanFormulation, 'notation'),
          html('p', item.leanModelMapping), html('p', item.leanModelLimitations, 'empty'));
      }
      if (item.description) det.append(html('p', item.description));
      (item.assumptions || []).forEach(a => det.append(html('p', 'Assumption: ' + a)));
      if (item.precondition) det.append(html('p', 'Precondition: ' + item.precondition));
      if (item.proofSketch) det.append(html('p', 'Proof sketch: ' + item.proofSketch));
      panel.append(det);
    });
  });
  if (n.basisInstantiation) {
    panel.append(html('h2', 'Interface instantiation'));
    panel.append(html('p', n.basisInstantiation));
  }
  if (n.specializationNote) {
    panel.append(html('h2', 'Specialization interface'));
    panel.append(html('p', n.specializationNote));
  }
  if (n.verificationObligation?.length) {
    panel.append(html('h2', 'Verification obligations'));
    n.verificationObligation.forEach(t => panel.append(html('p', t)));
  }
  panel.append(html('p', 'Coverage: ' + (n.coverageStatus || 'seed') + '. Empty sections indicate unrecorded material. Statements and proof sketches are not machine-checked proofs.', 'footer'));
}

function update() {
  $('view-description').textContent = viewDescriptions[view];
  document.querySelectorAll('[data-category]').forEach(n => n.setAttribute('aria-pressed', String(n.dataset.category === category)));
  const active = preview || pinned;
  const ve = visibleEdges();
  const neighbors = new Set();
  ve.forEach(e => {
    if (e.source === active) neighbors.add(e.target);
    if (e.target === active) neighbors.add(e.source);
  });
  edgeEls.forEach(({
    edge: e,
    element: p,
    marker
  }) => {
    p.style.display = ve.includes(e) ? '' : 'none';
    const incoming = active && e.target === active;
    const outgoing = active && e.source === active;
    const catEdge = category && (inCategory(all.get(e.source), category) || inCategory(all.get(e.target), category));
    p.setAttribute('class', 'edge' + (incoming ? ' incoming' : outgoing ? ' outgoing' : active || category && !catEdge ? ' dim' : ''));
    if (incoming || outgoing) p.setAttribute('marker-end', marker);else p.removeAttribute('marker-end');
  });
  nodeEls.forEach((group, id) => {
    const isActive = id === active;
    const isNeighbor = neighbors.has(id);
    const dim = active ? !isActive && !isNeighbor : category && !inCategory(all.get(id), category);
    group.setAttribute('class', 'node' + (isActive ? ' active' : isNeighbor ? ' neighbor' : dim ? ' dim' : ''));
    group.setAttribute('aria-pressed', String(id === pinned));
  });
  $('stats').textContent = `${shown.size} / ${concepts.length} concepts · ${ve.length} connections · ${subjectRoots.length} subjects · ${categories.length - subjectRoots.length} subsubject${categories.length - subjectRoots.length === 1 ? '' : 's'}`;
  renderDetails(active, edges.filter(e => enabled().has(e.type)));
  refreshLabels();
}

// Shared selection framing

// selection-camera:start
function selectionCamera(boxes, overview, step, backoff) {
  if (!boxes.length) return null;
  const x0 = Math.min(...boxes.map(b => b.x));
  const y0 = Math.min(...boxes.map(b => b.y));
  const x1 = Math.max(...boxes.map(b => b.x + b.width));
  const y1 = Math.max(...boxes.map(b => b.y + b.height));
  const familySpan = Math.max(180, (x1 - x0) * 1.15 + 48, (y1 - y0) * 1.15 + 48);
  return {
    x: (x0 + x1) / 2,
    y: (y0 + y1) / 2,
    span: Math.min(overview, familySpan * Math.pow(step, backoff))
  };
}
// selection-camera:end

// Camera movement and keyboard handling

function paintView() {
  svg.setAttribute('viewBox', `${viewCenter.x - viewSpan / 2} ${viewCenter.y - viewSpan / 2} ${viewSpan} ${viewSpan}`);
  refreshLabels();
}

function moveView(next, animate = true) {
  cancelAnimationFrame(animation);
  targetView = next;
  const start = {
    ...viewCenter,
    span: viewSpan
  };
  const began = performance.now();
  function frame(now) {
    const t = animate && !reducedMotion.matches ? Math.min(1, (now - began) / 550) : 1;
    const k = 1 - Math.pow(1 - t, 3);
    viewCenter = {
      x: start.x + (next.x - start.x) * k,
      y: start.y + (next.y - start.y) * k
    };
    viewSpan = start.span + (next.span - start.span) * k;
    paintView();
    if (t < 1) animation = requestAnimationFrame(frame);else animation = null;
  }
  animation = requestAnimationFrame(frame);
}

function fit() {
  const ys = [...positions.values()].map(p => p.y);
  moveView({
    x: 0,
    y: view === 'subject' ? 0 : (Math.min(...ys) + Math.max(...ys)) / 2,
    span: overviewSpan
  });
}

function focusSelection() {
  if (!pinned && !category) {
    fit();
    return;
  }
  let focus;
  if (pinned) {
    const family = view === 'dependency' ? edges.filter(e => e.type === 'requiresConcept' && (e.source === pinned || e.target === pinned)).flatMap(e => [e.source, e.target]) : children.get(pinned);
    focus = new Set([pinned, ...family]);
  } else focus = new Set(concepts.filter(n => inCategory(n, category)).map(n => n.id));
  const boxes = [...focus].filter(id => shown.has(id)).map(id => {
    const text = nodeEls.get(id).querySelector('text');
    const p = positions.get(id);
    wrapSvgLabel(text, all.get(id).shortForm, 180);
    const r = worldLabelRect(text);
    const x = Math.min(p.x - 8, r.left);
    const y = Math.min(p.y - 8, r.top);
    return {
      x,
      y,
      width: Math.max(p.x + 8, r.right) - x,
      height: Math.max(p.y + 8, r.bottom) - y
    };
  });
  // Concept families use a deliberately loose frame. Subjects already span
  // whole sectors, so that backoff would expand most selections to overview.
  const camera = selectionCamera(boxes, overviewSpan, zoomStep, pinned ? selectionZoomOutSteps : 0);
  if (camera) moveView(camera);else fit();
}

function zoom(factor, anchor) {
  const span = Math.min(overviewSpan * 1.5, Math.max(140, targetView.span / factor));
  const ratio = span / targetView.span;
  const at = anchor || {
    x: targetView.x,
    y: targetView.y
  };
  moveView({
    x: at.x + (targetView.x - at.x) * ratio,
    y: at.y + (targetView.y - at.y) * ratio,
    span
  });
}

function onKeyDown(event) {
  if (event.key === 'Escape') {
    clear();
    $('search').blur();
    return;
  }
  if (event.defaultPrevented || event.isComposing || event.repeat || event.ctrlKey || event.altKey || event.metaKey || event.key.toLowerCase() !== 'f') return;
  const editable = element => element instanceof Element && element.closest('input,textarea,select,[contenteditable]');
  if (editable(event.target) || editable(document.activeElement)) return;
  if (!graphPointerInside && !graphStage.contains(document.activeElement)) return;
  event.preventDefault();
  fit();
}

function endDrag() {
  drag = null;
  svg.style.cursor = '';
}

// SVG construction

function createArrowMarkers() {
  categories.forEach((c, i) => {
    const marker = el('marker', {
      id: `arrow-${i}`,
      viewBox: '0 0 10 10',
      refX: 9,
      refY: 5,
      markerWidth: 5,
      markerHeight: 5,
      orient: 'auto'
    });
    marker.append(el('path', {
      d: 'M 0 0 L 10 5 L 0 10 z',
      fill: colors.get(c.id)
    }));
    edgeDefs.append(marker);
  });
}

function createEdges() {
  edges.forEach((e, i) => {
    const gradient = el('linearGradient', {
      id: `edge-gradient-${i}`,
      gradientUnits: 'userSpaceOnUse',
      'color-interpolation': 'sRGB'
    });
    gradient.append(el('stop', {
      offset: '0%',
      'stop-color': colors.get(all.get(e.source).category[0])
    }), el('stop', {
      offset: '100%',
      'stop-color': colors.get(all.get(e.target).category[0])
    }));
    edgeDefs.append(gradient);
    const p = el('path', {
      class: 'edge',
      stroke: `url(#edge-gradient-${i})`
    });
    edgeGroup.append(p);
    edgeEls.push({
      edge: e,
      element: p,
      gradient,
      marker: `url(#arrow-${categories.findIndex(c => c.id === all.get(e.target).category[0])})`
    });
  });
}

function createConceptNodes() {
  concepts.forEach(n => {
    const group = el('g', {
      class: 'node',
      tabindex: '0',
      role: 'button',
      'aria-label': n.fullName,
      'aria-pressed': 'false'
    });
    group.append(el('circle', {
      cx: 0,
      cy: 0,
      r: 5.5,
      fill: colors.get(n.category[0])
    }));
    group.append(el('text', {
      x: 0,
      y: 0,
      dy: 3
    }, n.shortForm));
    group.append(el('title', {}, n.fullName));
    group.addEventListener('mouseenter', () => {
      preview = n.id;
      update();
    });
    group.addEventListener('mouseleave', () => {
      preview = null;
      update();
    });
    group.addEventListener('focus', () => {
      preview = n.id;
      update();
    });
    group.addEventListener('blur', () => {
      preview = null;
      update();
    });
    group.addEventListener('click', () => pick(n.id));
    group.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        pick(n.id);
      }
    });
    nodeGroup.append(group);
    nodeEls.set(n.id, group);
  });
}

function createGraph() {
  scene.append(membership, edgeGroup, nodeGroup, sectorGroup);
  createArrowMarkers();
  createEdges();
  createConceptNodes();
  scene.append(el('text', {
    x: 0,
    y: -8,
    'text-anchor': 'middle',
    class: 'center-title'
  }, 'MATHEMATICAL'));
  scene.append(el('text', {
    x: 0,
    y: 12,
    'text-anchor': 'middle',
    class: 'center-title'
  }, 'ABSTRACTIONS'));
}

// Event binding and startup

function bindEvents() {
  $('view-mode').addEventListener('change', changeView);
  $('search').addEventListener('input', options);
  $('search').addEventListener('keydown', e => {
    if (e.key === 'Enter' && $('concept-select').options.length > 1) pick($('concept-select').options[1].value);
  });
  $('concept-select').addEventListener('change', e => pick(e.target.value || null));
  $('reset').onclick = clear;
  $('filters').addEventListener('change', update);
  graphStage.addEventListener('pointerenter', () => {
    graphPointerInside = true;
  });
  graphStage.addEventListener('pointerleave', () => {
    graphPointerInside = false;
  });
  $('zoom-in').onclick = () => zoom(zoomStep);
  $('zoom-out').onclick = () => zoom(1 / zoomStep);
  $('fit').onclick = fit;
  svg.addEventListener('wheel', e => {
    e.preventDefault();
    const pt = new DOMPoint(e.clientX, e.clientY).matrixTransform(svg.getScreenCTM().inverse());
    zoom(Math.exp(-Math.max(-100, Math.min(100, e.deltaY)) * .002), pt);
  }, {
    passive: false
  });
  svg.addEventListener('pointerdown', e => {
    if (e.button !== 0 || e.target.closest('.node,.sector')) return;
    svg.focus({
      preventScroll: true
    });
    cancelAnimationFrame(animation);
    const pt = new DOMPoint(e.clientX, e.clientY).matrixTransform(svg.getScreenCTM().inverse());
    drag = pt;
    svg.setPointerCapture(e.pointerId);
    svg.style.cursor = 'grabbing';
  });
  svg.addEventListener('pointermove', e => {
    if (!drag) return;
    const pt = new DOMPoint(e.clientX, e.clientY).matrixTransform(svg.getScreenCTM().inverse());
    viewCenter = {
      x: viewCenter.x + drag.x - pt.x,
      y: viewCenter.y + drag.y - pt.y
    };
    targetView = {
      ...viewCenter,
      span: viewSpan
    };
    paintView();
  });
  svg.addEventListener('pointerup', endDrag);
  svg.addEventListener('pointercancel', endDrag);
  svg.addEventListener('lostpointercapture', endDrag);
  new ResizeObserver(showLabelPreview).observe(svg);
  document.fonts.ready.then(() => {
    labelPlan = null;
    refreshLabels();
  });
  document.addEventListener('keydown', onKeyDown);
}

function initialize() {
  createGraph();
  bindEvents();
  options();
  layout();
  update();
  moveView({
    x: 0,
    y: 0,
    span: overviewSpan
  }, false);
}
initialize();
