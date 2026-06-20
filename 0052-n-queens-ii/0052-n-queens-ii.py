class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        postDiag=set()
        negDiag=set()
        res=0
        def backtrack(r):
            if r==n:
                nonlocal res
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in postDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                postDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1)
                col.remove(c)
                postDiag.remove(r+c)
                negDiag.remove(r-c)
                
        backtrack(0)
        return res
