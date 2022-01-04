#!/usr/bin/env python3

import unittest

def pascal_rows(n: int) -> list[list[int]]:
    """Returns the first N rows of Pascal's triangle."""
    rows = [[1]]
    if n > 1:
        pascal_helper(n - 1, rows)
    return rows

def pascal_helper(k: int, rows: list[list[int]]):
    """Add a new row based on the last row."""
    if k < 1:
        return
    last_row = rows[-1]
    next_len = len(last_row) + 1
    next_row = [0] * next_len
    for i in range(next_len):
        left = 0 if i == 0 else last_row[i - 1]
        right = 0 if i == next_len - 1 else last_row[i]
        next_row[i] = left + right
    rows.append(next_row)
    pascal_helper(k - 1, rows)
    
class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pascal_rows(1), [[1]])
    def test_2(self):
        self.assertEqual(pascal_rows(2), [[1], [1, 1]])
    def test_3(self):
        self.assertEqual(pascal_rows(3), [[1], [1, 1], [1, 2, 1]])

if __name__ == "__main__":
    unittest.main()

# Local Variables:
# mode: python
# End:
