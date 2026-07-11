class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            if not visited[i]:
          
                comp = []
                queue = [i]
                visited[i] = True
                
                for node in queue:
                    comp.append(node)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
       
                k = len(comp)
                if all(len(adj[v]) == k - 1 for v in comp):
                    ans += 1
                    
        return ans
        