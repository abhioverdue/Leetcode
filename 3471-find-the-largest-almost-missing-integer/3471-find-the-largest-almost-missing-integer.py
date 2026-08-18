class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        n = len(nums)
        subarray_count = defaultdict(set)
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            for num in set(subarray):
                subarray_count[num].add(i)
        ans = -1
        for num, idx_set in subarray_count.items():
            if len(idx_set) == 1:
                ans = max(ans, num)
                
        return ans