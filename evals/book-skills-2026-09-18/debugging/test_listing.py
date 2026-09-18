import importlib
import unittest

import listing


class PageTests(unittest.TestCase):
    def setUp(self):
        importlib.reload(listing)

    def test_first_call_defaults(self):
        self.assertEqual(listing.page('items', [0, 1, 2]), [0, 1])

    def test_same_key_next_page(self):
        rows = [0, 1, 2, 3, 4, 5]
        self.assertEqual(listing.page('items', rows), [0, 1])
        self.assertEqual(listing.page('items', rows, 2, 2), [2, 3])

    def test_same_key_changed_limit(self):
        rows = [0, 1, 2, 3]
        listing.page('items', rows)
        self.assertEqual(listing.page('items', rows, 0, 3), [0, 1, 2])

    def test_same_key_replaced_rows(self):
        listing.page('items', [0, 1, 2])
        self.assertEqual(listing.page('items', [10, 11, 12]), [10, 11])

    def test_same_key_mutated_rows(self):
        rows = [0, 1, 2]
        listing.page('items', rows)
        rows[0] = 99
        self.assertEqual(listing.page('items', rows), [99, 1])

    def test_empty_and_out_of_range_then_tail(self):
        self.assertEqual(listing.page('items', []), [])
        self.assertEqual(listing.page('items', [0, 1, 2], 3, 2), [])
        self.assertEqual(listing.page('items', [0, 1, 2], 100, 2), [])
        self.assertEqual(listing.page('items', [0, 1, 2], 2, 10), [2])

    def test_tuple_input_returns_list(self):
        result = listing.page('items', (0, 1, 2), 1, 1)
        self.assertIs(type(result), list)
        self.assertEqual(result, [1])

    def test_return_container_is_independent(self):
        rows = [0, 1, 2]
        result = listing.page('items', rows)
        result.append(42)
        self.assertEqual(rows, [0, 1, 2])
        self.assertEqual(listing.page('items', rows), [0, 1])


if __name__ == '__main__':
    unittest.main()
