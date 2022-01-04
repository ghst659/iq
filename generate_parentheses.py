#!/usr/bin/env python3

# Given n pairs of parentheses, write a function to generate all
# combinations of well-formed parentheses.
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return []

def allsums(n: int) -> list[list[int]]:
    """Generates a list of equal-sum lists."""
    if not n:
        return []
    result = []
    for k in range(n):
        pass

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self._s = Solution()

    def tearDown(self):
        del self._s

    def test_example1(self):
        self.assertEqual(self._s.generateParenthesis(3),
                         ["((()))","(()())","(())()","()(())","()()()"])

    def test_example2(self):
        self.assertEqual(self._s.generateParenthesis(1),
                         ["()"])

if __name__ == "__main__":
    unittest.main()

# Local Variables:
# mode: python
# End:
