class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        i = 0
        n -= 1
        while n:
            while (ans >> i) & 1 != 0:
                i += 1
            ans = ans | ((n & 1) << i)  # Added parentheses here
            n = n >> 1
            i += 1
        return ans