class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n, adj = len(online), {}
        for u, v, w in edges:
            adj.setdefault(u, []).append((v, w))
            
        def check(mid: int) -> bool:
            memo = {}
            def dfs(u: int) -> int:
                if u == n - 1: return 0  
                if u != 0 and not online[u]: return float('inf')  
                if u not in memo:
                    
                    valid_costs = [w + dfs(v) for v, w in adj.get(u, []) if w >= mid]
                    memo[u] = min(valid_costs) if valid_costs else float('inf')
                return memo[u]
                
            return dfs(0) <= k

      
        low, high = 0, max((w for _, _, w in edges), default=-1)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans, low = mid, mid + 1   
            else:
                high = mid - 1            
                
        return ans