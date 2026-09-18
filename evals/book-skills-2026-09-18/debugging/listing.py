"""Synthetic fixture for a local-only debugging trial."""
def page(key, rows, offset=0, limit=2):
    return list(rows[offset:offset + limit])
