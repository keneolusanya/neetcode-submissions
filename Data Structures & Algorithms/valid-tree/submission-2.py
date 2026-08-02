class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i : [] for i in range(n)}
        seen = set()

        # back and forth involving three or mor enodes
        # what if you basically ignored a most recently
        # relevant node when processsing?
       

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, par):
            if node in seen and node != par:
                return False

            seen.add(node)

            for u in adj[node]:
                if u != par:
                    if not dfs(u, node):
                        return False

            return True
        
        return dfs(0, None) and len(seen) == n