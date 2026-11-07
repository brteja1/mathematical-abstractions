"""Structural checks for the catalog's documented mathematical interfaces."""
from pathlib import Path
import json
from datetime import date

LINK_TYPES = {
    'category': {'Category'}, 'kind': {'ConceptKind'},
    'requiresConcept': {'Concept'}, 'specializationOf': {'Concept'},
    'relatedConcept': {'Concept'}, 'hasOperation': {'Operation'},
    'hasAxiom': {'Axiom'}, 'hasLaw': {'Law'}, 'hasTheorem': {'Theorem'},
    'source': {'Source'}, 'concept': {'Concept'}, 'appliesTo': {'Concept'},
    'dependsOn': {'Axiom', 'Law', 'Theorem', 'Operation'},
}
CLAIMS = {'Axiom', 'Law', 'Theorem'}

def validate(doc):
    baseline=json.loads((Path(__file__).resolve().parents[1]/'provenance_legacy.json').read_text())
    legacy_missing=set(baseline['missingSourceIds'])
    legacy_cited=set(baseline['existingCitedIds'])
    legacy_sources=set(baseline['existingSourceIds'])
    errors=[]
    manifest_path=Path(__file__).resolve().parents[1]/'data/import_manifest.json'
    if manifest_path.exists():
        frozen=json.loads(manifest_path.read_text())['provenanceBaseline']
        for key in ['missingSourceIds','existingCitedIds','existingSourceIds']:
            added=set(baseline[key])-set(frozen[key])
            if added: errors.append('Provenance baseline cannot be extended: '+key)
        for key in ['existingCitedIds','existingSourceIds']:
            if set(frozen[key])-set(baseline[key]):
                errors.append('Existing citation baseline cannot be reduced: '+key)
    graph=doc.get('@graph')
    if not isinstance(graph,list): return ['@graph must be an array']
    index={}
    for n in graph:
        if not isinstance(n,dict) or not isinstance(n.get('id'),str):
            errors.append('Each graph node must be an object with a string id'); continue
        if n['id'] in index: errors.append('Duplicate ID: '+n['id'])
        index[n['id']]=n
    names=set()
    for ident,n in index.items():
        kind=n.get('type')
        for key,expected in LINK_TYPES.items():
            if key not in n: continue
            values=n[key] if isinstance(n[key],list) else [n[key]]
            for ref in values:
                if not isinstance(ref,str) or ref not in index:
                    errors.append(f'{ident}: dangling {key}: {ref}'); continue
                if index[ref].get('type') not in expected:
                    errors.append(f'{ident}: wrong target type for {key}: {ref}')
        fields=[]
        if kind=='Concept':
            fields=['shortForm','fullName','category','kind','definition','notation','axiomBasis','basisKind','basisScope','coverageStatus']
            name=n.get('shortForm')
            if isinstance(name,str):
                if name in names:errors.append('Duplicate shortForm: '+name)
                names.add(name)
            for key in ['hasOperation','hasAxiom','hasLaw','hasTheorem']:
                if not isinstance(n.get(key),list):errors.append(f'{ident}: {key} must be an array')
            if not n.get('hasAxiom'):errors.append(f'{ident}: no recorded defining rules')
            if not n.get('hasOperation') and not n.get('noPrimitiveOperationsReason'):
                errors.append(f'{ident}: missing operations or noPrimitiveOperationsReason')
            if not n.get('hasLaw') and not n.get('hasTheorem'):
                errors.append(f'{ident}: no recorded derived results')
            for key in ['hasAxiom','hasLaw','hasTheorem']:
                for ref in n.get(key,[]) if isinstance(n.get(key),list) else []:
                    if ref in index and ident not in index[ref].get('appliesTo',[]):
                        errors.append(f'{ident}: {ref} does not apply to its linked concept')
            for ref in n.get('hasOperation',[]):
                if ref in index and index[ref].get('concept')!=ident:
                    errors.append(f'{ident}: operation ownership mismatch: {ref}')
        elif kind=='Operation':fields=['name','signature','description','concept']
        elif kind in CLAIMS:
            fields=['statement','formalStatement','assumptions','appliesTo','reviewStatus']
            if kind=='Axiom':fields+=['ruleRole']
        if kind in {'Concept','Axiom','Law','Theorem'}:
            sources=n.get('source')
            if not sources:
                if ident not in legacy_missing:
                    errors.append(f'{ident}: missing required source')
                elif n.get('provenanceStatus')!='legacy-source-missing':
                    errors.append(f'{ident}: legacy source gap must be disclosed')
            elif not isinstance(sources,list):
                errors.append(f'{ident}: source must be a nonempty array of Source IDs')
            if ident not in legacy_missing and ident not in legacy_cited:
                for key in ['sourceLocator','sourceNote','provenanceKind']:
                    if not n.get(key):errors.append(f'{ident}: missing provenance field {key}')
                if n.get('provenanceKind') not in {'direct','adapted','derived'}:
                    errors.append(f'{ident}: provenanceKind must be direct, adapted, or derived')
                if n.get('provenanceKind')=='derived' and not n.get('dependsOn') and kind!='Concept':
                    errors.append(f'{ident}: derived claim needs explicit dependsOn premises')
        if kind=='Source':
            if not n.get('label'):errors.append(f'{ident}: Source needs a title in label')
            if not any(n.get(k) for k in ['url','path','citation']):
                errors.append(f'{ident}: Source needs url, path, or bibliographic citation')
            if ident not in legacy_sources:
                for key in ['accessedOn','sourceRole']:
                    if not n.get(key):errors.append(f'{ident}: new Source missing {key}')
                if n.get('accessedOn'):
                    try:
                        parsed=date.fromisoformat(n['accessedOn'])
                        if parsed.isoformat()!=n['accessedOn']:raise ValueError('noncanonical date')
                    except (ValueError, TypeError):
                        errors.append(f'{ident}: accessedOn must be YYYY-MM-DD')
        for key in fields:
            if not n.get(key):errors.append(f'{ident}: missing or empty {key}')
    # Specializations form a hierarchy; prerequisites and related links may cycle.
    hierarchy_done=set(); hierarchy_active=set()
    def visit_specialization(ident):
        if ident in hierarchy_active:
            errors.append('Cyclic specialization: '+ident);return
        if ident in hierarchy_done:return
        hierarchy_active.add(ident)
        refs=index[ident].get('specializationOf',[])
        if isinstance(refs,str):refs=[refs]
        seen=set()
        for ref in refs:
            if not isinstance(ref,str):continue
            if ref in seen:errors.append(f'{ident}: duplicate specializationOf: {ref}')
            seen.add(ref)
            if ref in index and index[ref].get('type')=='Concept':visit_specialization(ref)
        hierarchy_active.remove(ident);hierarchy_done.add(ident)
    for ident,n in index.items():
        if n.get('type')=='Concept':visit_specialization(ident)
    # Derivation edges must also be acyclic.
    visited=set(); active=set()
    def visit(ident):
        if ident in active:errors.append('Cyclic claim dependency: '+ident);return
        if ident in visited:return
        active.add(ident)
        for ref in index[ident].get('dependsOn',[]):
            if isinstance(ref,str) and ref in index:visit(ref)
        active.remove(ident);visited.add(ident)
    for ident in index:visit(ident)
    return errors
