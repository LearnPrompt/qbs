import platform
import sys

import original_listing as listing

print('Python:', sys.version.split()[0])
print('Platform:', platform.platform())
rows = [0, 1, 2, 3, 4, 5]
print('first:', listing.page('items', rows))
print('same-key offset=2:', listing.page('items', rows, 2, 2))
print('direct slice offset=2:', list(rows[2:4]))
print('new-key offset=2:', listing.page('other', rows, 2, 2))
print('same-key limit=3:', listing.page('items', rows, 0, 3))
print('same-key replacement:', listing.page('items', [10, 11, 12]))
rows[0] = 99
print('same-key mutation:', listing.page('items', rows))
print('cache contents:', listing._cache)
listing._cache.clear()
print('after clearing state, offset=2:', listing.page('items', rows, 2, 2))
