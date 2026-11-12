"""Task-sized views of authoritative records; never clip semantic conditions."""

VIEWS = ('focused', 'lean', 'full')
INTERFACE_LINKS = {'hasOperation', 'hasAxiom', 'hasLaw', 'hasTheorem'}
LEAN_FIELDS = {'leanFormulation', 'leanModelMapping', 'leanPremiseMapping',
               'formulationSource', 'formulationLocator'}
PROOF_FIELDS = {'proofSketch'}


def record_view(record, view='focused', selected_links=()):
    """Keep all assumptions/guards; omit unrelated claims and opt-in proof text.

    `full` is the lossless canonical record for auditing. `lean` adds the typed
    formulation for the selected record, without expanding other claims.
    """
    if view not in VIEWS:
        raise ValueError('Record view must be focused, lean or full')
    if view == 'full':
        return dict(record)
    excluded = PROOF_FIELDS | (INTERFACE_LINKS - set(selected_links))
    if view == 'focused':
        excluded |= LEAN_FIELDS
    return {key: value for key, value in record.items() if key not in excluded}
