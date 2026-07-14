import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)

        dp = {}
        dp[(0, 0)] = 1
     
        gcd_memo = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        for i in range(max_val + 1):
            for j in range(max_val + 1):
                gcd_memo[i][j] = math.gcd(i, j)

        for x in nums:
            next_dp = dp.copy()
            for (g1, g2), count in dp.items():
                
                ng1 = gcd_memo[g1][x]
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                ng2 = gcd_memo[g2][x]
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = next_dp
            
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + count) % MOD
                
        return ans