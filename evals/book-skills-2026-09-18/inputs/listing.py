"""Synthetic fixture for a local-only debugging trial."""
_cache = {}


def page(key, rows, offset=0, limit=2):
    if key not in _cache:
        _cache[key] = list(rows[offset:offset + limit])
    return list(_cache[key])
