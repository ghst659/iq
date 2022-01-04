#!/usr/bin/env python3

import typing
import unittest

def pascal_rows(n: int) -> list[tuple[int]]:
    result = []
    for row in generate_rows(n):
        result.append(row)
    return result
    
def generate_rows(n: int) -> typing.Generator[tuple[int], None, None]:
    """Yields successive rows of Pascal's triangle."""
    row = [1]
    for i in range(n):
        last_row = row
        last_len= len(last_row)
        yield tuple(row)
        row = [0] * (last_len + 1)
        for i in range(last_len + 1):
            left = 0 if i == 0 else last_row[i - 1]
            right = 0 if i == last_len else last_row[i]
            row[i] = left + right

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pascal_rows(1),
                         [(1,)])
    def test_2(self):
        self.assertEqual(pascal_rows(2),
                         [(1,), (1, 1)])
    def test_3(self):
        self.assertEqual(pascal_rows(3),
                         [(1,), (1, 1), (1, 2, 1)])
    def test_4(self):
        self.assertEqual(pascal_rows(4),
                         [(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1)])

if __name__ == "__main__":
    unittest.main()

# Local Variables:
# mode: python
# End:
