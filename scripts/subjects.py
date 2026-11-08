"""Subject navigation over explicit category links; no mathematical inheritance."""


def category_path(index, ident):
    path, seen = [], set()
    while ident:
        if ident in seen:
            raise ValueError('Cyclic category hierarchy: ' + ident)
        seen.add(ident)
        node = index[ident]
        if node.get('type') != 'Category':
            raise ValueError('Expected category: ' + ident)
        path.insert(0, ident)
        ident = node.get('parentCategory')
    return path


def in_category(index, concept, query):
    """Match a full category ID or short suffix, including its descendants."""
    return any(ident == query or ident.endswith('/' + query)
               for category in concept['category']
               for ident in category_path(index, category))
