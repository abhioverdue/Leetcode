class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor=reduce(operator.xor, nums,0)
        if total_xor!=0:
            return len(nums)
        return 0 if all(x==0 for x in nums) else len(nums)-1