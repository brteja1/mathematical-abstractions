// Browser-only checks use actual SVG geometry, font metrics and transforms.
const labelChecks=[];
function assertLabel(ok,message){if(!ok)throw new Error(message);labelChecks.push(message);}
function settleLabels(){cancelAnimationFrame(animation);viewCenter={x:targetView.x,y:targetView.y};viewSpan=targetView.span;paintView();refreshLabels();}
function renderedLabels(){return [...document.querySelectorAll('#graph .node text,#graph .sector text')].filter(t=>t.style.visibility==='visible'&&t.closest('.node')?.style.display!=='none');}
function verifySubjectHeadings(where){
 for(const group of sectorGroup.querySelectorAll('.sector')){
  const id=group.dataset.category,expected=!all.get(id).parentCategory||id===category;
  assertLabel((group.querySelector('text').style.visibility==='visible')===expected,where+': only root or selected subject headings are visible');
  if(all.get(id).parentCategory){
   const text=group.querySelector('text');assertLabel(text.querySelectorAll('tspan').length===1&&text.textContent===all.get(id).label,where+': nested subject name is complete on one line');
   const parent=sectorGroup.querySelector(`[data-category="${all.get(id).parentCategory}"]`);
   const arcRadius=element=>Number(element.querySelector('path').getAttribute('d').match(/ A([^,]+),/)[1]);
   const expectedRadius=(arcRadius(group)+arcRadius(parent))/2;
   const matrix=labelTransformMatrix(text),anchor=new DOMPoint(Number(text.getAttribute('x')),Number(text.getAttribute('y'))).matrixTransform(matrix);
   assertLabel(Math.abs(Math.hypot(anchor.x,anchor.y)-expectedRadius)<.01,where+': nested name stays exactly halfway between parent and child arcs');
   const style=getComputedStyle(text);labelContext.font=`${style.fontStyle} ${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
   const ink=labelContext.measureText(all.get(id).label);
   assertLabel(Math.abs(Number(text.querySelector('tspan').getAttribute('dy'))-(ink.actualBoundingBoxAscent-ink.actualBoundingBoxDescent)/2)<1e-7,where+': text ink is centered on the gap anchor');
  }
 }
}
function verifyLabels(where){
 verifySubjectHeadings(where);
 assertLabel(nodeEls.size===concepts.length,where+': every concept has a graph node');
 for(const [id,group] of nodeEls){
  const text=group.querySelector('text'),r=text.getBoundingClientRect();
  assertLabel(group.style.display!=='none'&&text.style.visibility==='visible',where+': every name is visible');
  assertLabel(text.textContent===all.get(id).shortForm,where+': concept name is complete and untruncated');
  assertLabel(Number.isFinite(r.left)&&Number.isFinite(r.top),where+': label has finite geometry');
 }
}
function nodeCoordinates(){return JSON.stringify([...nodeEls].map(([id,g])=>[id,g.querySelector('circle').getAttribute('cx'),g.querySelector('circle').getAttribute('cy')]));}
function runLabelChecks(){
 const id=name=>'urn:csabs:concept/'+name;
 settleLabels();const before=nodeCoordinates();
 assertLabel(window.viewerErrors.length===0,'page initializes');
 assertLabel(!$('show-labels'),'name toggle has been removed');
 assertLabel(!$('categories'),'redundant subject list has been removed');
 assertLabel([...nodeEls.values()].every(g=>g.querySelector('text').style.visibility==='visible'),'overview displays every concept name');
 assertLabel(concepts.filter(n=>!children.get(n.id).length).every(n=>nodeEls.get(n.id).querySelector('text').style.visibility==='visible'),'every leaf concept name is visible');
 assertLabel(renderedLabels().length>0,'subject labels remain available');verifyLabels('overview');
 const nested='urn:csabs:category/locks',otherNested='urn:csabs:category/sequential-collections';
 showCategory(nested);settleLabels();verifyLabels('selected nested subject');
 assertLabel(sectorGroup.querySelector(`[data-category="${nested}"] text`).style.visibility==='visible','selected nested heading is shown');
 assertLabel(sectorGroup.querySelector('[data-category="urn:csabs:category/synchronization"] text').style.visibility==='hidden','unselected middle ancestor remains hidden');
 showCategory(otherNested);settleLabels();verifyLabels('another nested subject');
 assertLabel(sectorGroup.querySelector(`[data-category="${nested}"] text`).style.visibility==='hidden','previous nested heading hides after selection changes');
 pick(id('Mutex'));settleLabels();verifyLabels('concept selection clears nested headings');
 clear();settleLabels();

 showCategory('urn:csabs:category/data-structures');settleLabels();
 assertLabel([...nodeEls.values()].every(g=>g.querySelector('text').style.visibility==='visible'),'subject selection retains every concept name');
 assertLabel(nodeCoordinates()===before,'label wrapping and placement preserve graph coordinates');verifyLabels('dense subject');
 const transforms=[...document.querySelectorAll('.sector text')].map(t=>t.getAttribute('transform')).join('|');refreshLabels();refreshLabels();
 assertLabel(transforms===[...document.querySelectorAll('.sector text')].map(t=>t.getAttribute('transform')).join('|'),'placements do not drift on refresh');
 const snapshot=()=>JSON.stringify([...document.querySelectorAll('#graph .node text,#graph .sector text')].map(t=>[t.style.visibility,t.getAttribute('transform'),t.textContent,t.getBoundingClientRect().width]));
 const background=snapshot();
 for(const name of ['Mutex','Group','Sequence','BinaryTree']){
  nodeEls.get(id(name)).dispatchEvent(new Event('mouseenter'));
  assertLabel(snapshot()===background,'hover preserves all background labels: '+name);
  assertLabel(!$('label-preview').hidden&&$('label-preview').textContent===all.get(id(name)).fullName,'hover callout names the concept');
  nodeEls.get(id(name)).dispatchEvent(new Event('mouseleave'));
  assertLabel(snapshot()===background,'hover exit preserves all background labels: '+name);
 }
 const beforeFocus=snapshot();
 nodeEls.get(id('Mutex')).dispatchEvent(new Event('focus'));
 assertLabel(snapshot()===beforeFocus,'keyboard focus preserves the background plan');
 settleLabels();
 assertLabel(!$('label-preview').hidden&&$('label-preview').textContent===all.get(id('Mutex')).fullName,'keyboard focus reveals a full-name callout');
 assertLabel($('details').textContent.includes(all.get(id('Mutex')).fullName),'full name available through keyboard focus');verifyLabels('focused concept');
 nodeEls.get(id('Mutex')).dispatchEvent(new Event('blur'));
 clear();settleLabels();
 const at=positions.get(id('Group'));
 const planSnapshot=()=>JSON.stringify([...document.querySelectorAll('#graph .node text,#graph .sector text')].map(t=>[t.style.visibility,t.getAttribute('transform'),t.textContent]));
 const overviewPlan=planSnapshot();
 for(const ratio of [1.1,2.1,2.3,1.9,3.5,.8]){
  moveView({x:at.x,y:at.y,span:overviewSpan/ratio},false);settleLabels();
  assertLabel(planSnapshot()===overviewPlan,'camera motion never changes label visibility, wrapping or anchors');
 }
 assertLabel([...nodeEls.values()].every(g=>g.querySelector('text').style.visibility==='visible'),'zoom retains every concept name');
 const allPlan=planSnapshot();
 for(const ratio of [1,2,3,.7]){moveView({x:at.x+300,y:at.y-180,span:overviewSpan/ratio},false);settleLabels();assertLabel(planSnapshot()===allPlan,'all names remain fixed during zoom and pan');}
 const originalWidth=svg.style.width;svg.style.width=(svg.getBoundingClientRect().width-24)+'px';refreshLabels();
 assertLabel(planSnapshot()===allPlan,'resize does not repack names');svg.style.width=originalWidth;refreshLabels();
 const currentWidth=svg.getBoundingClientRect().width;svg.style.width=(currentWidth+18)+'px';refreshLabels();assertLabel(planSnapshot()===allPlan,'growing canvas preserves the plan');svg.style.width=originalWidth;
 clear();settleLabels();
 for(const mode of ['specialization','dependency']){
  clear();settleLabels();$('view-mode').value=mode;$('view-mode').dispatchEvent(new Event('change'));settleLabels();pick(id('FirstOrderNaturalDeduction'));settleLabels();
  const text=nodeEls.get(id('FirstOrderNaturalDeduction')).querySelector('text');
  assertLabel(text.querySelectorAll('tspan').length>1,mode+': long name wraps');
  assertLabel(text.style.visibility==='visible',mode+': selected label remains visible');
  assertLabel([...text.querySelectorAll('tspan')].every(line=>line.getComputedTextLength()<=181),mode+': wrapping uses actual font widths');
  const selectedPlan=planSnapshot();moveView({x:100,y:200,span:overviewSpan/3},false);settleLabels();pick(id('FirstOrderNaturalDeduction'));settleLabels();assertLabel(planSnapshot()===selectedPlan,mode+': same selection produces the same plan at different zoom levels');
  verifyLabels(mode);
 }

 // All selection entrypoints use the same camera policy and preserve repeated selections.
 clear();settleLabels();$('view-mode').value='subject';$('view-mode').dispatchEvent(new Event('change'));settleLabels();
 const topic='urn:csabs:category/locks',subtree='urn:csabs:category/synchronization';
 const arc=()=>sectorGroup.querySelector(`[data-category="${topic}"]`);
 const sameCamera=(a,b)=>['x','y','span'].every(key=>Math.abs(a[key]-b[key])<1e-7);
 arc().dispatchEvent(new MouseEvent('click',{bubbles:true}));
 const arcCamera={...targetView};
 assertLabel(category===topic&&!pinned,'sub-topic arc selects its subject');
 assertLabel(arcCamera.span<overviewSpan,'sub-topic arc zooms into its members');
 settleLabels();arc().dispatchEvent(new MouseEvent('click',{bubbles:true}));
 assertLabel(category===topic&&sameCamera(targetView,arcCamera),'repeated topic click refocuses without deselecting');settleLabels();
 clear();settleLabels();arc().dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}));
 assertLabel(sameCamera(targetView,arcCamera),'keyboard topic selection uses the same framing');settleLabels();
 showCategory(subtree);settleLabels();
 const parentCamera={...targetView};assertLabel(category===subtree&&!pinned,'parent topic selection includes descendants');
 const topicMembers=concepts.filter(n=>inCategory(n,subtree));assertLabel(topicMembers.some(n=>n.id===id('LamportBakery')),'parent focus includes nested protocol members');
 showCategory(topic);settleLabels();
 const paneButton=[...$('details').querySelectorAll('.relation-button')].find(b=>b.textContent===all.get(id('Mutex')).fullName);
 paneButton.click();const paneCamera={...targetView};assertLabel(pinned===id('Mutex'),'right pane selects the concept');settleLabels();
 clear();settleLabels();nodeEls.get(id('Mutex')).dispatchEvent(new MouseEvent('click',{bubbles:true}));
 assertLabel(pinned===id('Mutex')&&sameCamera(targetView,paneCamera),'graph concept click matches right-pane camera');settleLabels();
 nodeEls.get(id('Mutex')).dispatchEvent(new MouseEvent('click',{bubbles:true}));
 assertLabel(pinned===id('Mutex')&&sameCamera(targetView,paneCamera),'repeated concept click refocuses without clearing');settleLabels();
 nodeEls.get(id('Mutex')).dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}));
 assertLabel(sameCamera(targetView,paneCamera),'keyboard concept selection matches right pane');settleLabels();
 showCategory(subtree);settleLabels();
 assertLabel(sameCamera(targetView,parentCamera),'returning to a topic restores identical framing');
 document.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape'}));settleLabels();
 assertLabel(category===null&&pinned===null&&targetView.span===overviewSpan,'escape restores the overview');
 // F shares the Fit button behavior and is scoped to the graph viewport.
 const pressFit=(target,key='f',extra={})=>target.dispatchEvent(new KeyboardEvent('keydown',{key,bubbles:true,cancelable:true,...extra}));
 for(const mode of ['subject','specialization','dependency']){
  $('view-mode').value=mode;$('view-mode').dispatchEvent(new Event('change'));settleLabels();
  $('fit').click();const expectedFit={...targetView};settleLabels();
  moveView({x:180,y:-120,span:overviewSpan/3},false);settleLabels();
  svg.focus();pressFit(svg);assertLabel(sameCamera(targetView,expectedFit),mode+': F matches Fit with keyboard focus');settleLabels();
 }
 moveView({x:180,y:-120,span:overviewSpan/3},false);settleLabels();
 $('fit').click();const hoverFit={...targetView};settleLabels();moveView({x:180,y:-120,span:overviewSpan/3},false);settleLabels();
 $('reset').focus();graphStage.dispatchEvent(new Event('pointerenter'));pressFit(document,'F');
 assertLabel(sameCamera(targetView,hoverFit),'uppercase F fits while pointer is over graph');settleLabels();
 moveView({x:180,y:-120,span:overviewSpan/3},false);settleLabels();const unchangedFit={...targetView};
 $('search').focus();pressFit($('search'));assertLabel(sameCamera(targetView,unchangedFit),'typing f in search does not fit');
 svg.focus();pressFit(svg,'f',{ctrlKey:true});assertLabel(sameCamera(targetView,unchangedFit),'Ctrl+F retains browser behavior');
 pressFit(svg,'f',{metaKey:true});assertLabel(sameCamera(targetView,unchangedFit),'Meta+F retains browser behavior');
 graphStage.dispatchEvent(new Event('pointerleave'));$('reset').focus();pressFit(document);
 assertLabel(sameCamera(targetView,unchangedFit),'F outside graph does not fit');

 nodeEls.forEach((g,id)=>assertLabel(g.getAttribute('aria-label')===all.get(id).fullName&&g.querySelector('title').textContent===all.get(id).fullName,'full names retained for accessible nodes'));
 clear();settleLabels();$('view-mode').value='subject';$('view-mode').dispatchEvent(new Event('change'));settleLabels();
 if(window.labelScenario==='nested'){showCategory('urn:csabs:category/sequential-collections');settleLabels();}
 if(window.labelScenario==='dense'){showCategory('urn:csabs:category/data-structures');settleLabels();}
 if(window.labelScenario==='selected'){$('view-mode').value='specialization';$('view-mode').dispatchEvent(new Event('change'));pick(id('FirstOrderNaturalDeduction'));settleLabels();}
 assertLabel(window.viewerErrors.length===0,'no browser errors');
 return {ok:true,checks:labelChecks.length,viewport:innerWidth,visibleLabels:renderedLabels().length};
}
try {const report=document.createElement('pre');report.id='label-report';report.hidden=true;report.textContent=JSON.stringify(runLabelChecks());document.body.append(report);}catch(error){const report=document.createElement('pre');report.id='label-report';report.textContent=JSON.stringify({ok:false,error:String(error),completed:labelChecks});document.body.append(report);}
