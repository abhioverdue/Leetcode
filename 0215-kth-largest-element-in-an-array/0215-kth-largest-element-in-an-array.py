import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(arr, target):
            pivot = random.choice(arr)
            left  = [x for x in arr if x > pivot]  
            mid   = [x for x in arr if x == pivot]  
            right = [x for x in arr if x < pivot]  
  
            if target <= len(left):
  
                return quickselect(left, target)
            elif target <= len(left) + len(mid):
 
                return pivot
            else:
    
                return quickselect(right, target - len(left) - len(mid))
        return quickselect(nums, k)