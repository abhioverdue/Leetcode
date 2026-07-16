import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        current_max = 0
        for x in nums:
            if x > current_max:
                current_max = x
            prefix_gcd.append(math.gcd(x, current_max))
        
        prefix_gcd.sort()
        
        left = 0
        right = n - 1
        total_gcd_sum = 0
        
        while left < right:
            total_gcd_sum += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return total_gcd_sum