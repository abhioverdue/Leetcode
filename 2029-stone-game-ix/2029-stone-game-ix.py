class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c=collections.Counter(x%3 for x in stones)
        if c[0]%2==0:
            return c[1]>=1 and c[2]>=1
        return abs(c[1]-c[2])>2