class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
            
        ans = float('inf')
        q = deque([1])
        visited = {1}
        
        while q:
            node = q.popleft()
            for neighbor, dist in adj[node]:
                ans = min(ans, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    
        return ans
        