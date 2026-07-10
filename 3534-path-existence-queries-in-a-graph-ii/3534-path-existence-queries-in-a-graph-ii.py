class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nodes = sorted((val, idx) for idx, val in enumerate(nums))
        sorted_vals = [val for val, _ in sorted_nodes]
   
        pos_map = [0] * n
        for s_idx, (_, o_idx) in enumerate(sorted_nodes):
            pos_map[o_idx] = s_idx
            
        LOG = 18 
        up = [[0] * LOG for _ in range(n)]

        for i in range(n):
            up[i][0] = bisect.bisect_right(sorted_vals, sorted_vals[i] + maxDiff) - 1
            
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            pos_u, pos_v = pos_map[u], pos_map[v]
            if pos_u > pos_v:
                pos_u, pos_v = pos_v, pos_u
       
            if up[pos_u][LOG - 1] < pos_v:
                ans.append(-1)
                continue
                
            steps = 0
            curr = pos_u
            for j in range(LOG - 1, -1, -1):
                if up[curr][j] < pos_v:
                    steps += (1 << j)
                    curr = up[curr][j]
                    
            ans.append(steps + 1)
            
        return ans