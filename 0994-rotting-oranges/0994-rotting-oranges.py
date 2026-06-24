class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time,fresh=0,0
        ROWS,COLS=len(grid),len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    rows,cols=dr+r,dc+c
                    if (rows<0 or rows==len(grid) or cols<0 or cols==len(grid[0]) or grid[rows][cols]!=1):
                        continue
                    grid[rows][cols]=2
                    q.append([rows,cols])
                    fresh-=1
            if q:
                time+=1
        return time if fresh==0 else -1