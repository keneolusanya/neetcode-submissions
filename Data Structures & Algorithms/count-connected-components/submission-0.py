class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adjacency list
        # dfs
        # seen set
        # then you're like, if not in seen, you do dfs and like add to a res variable
        adj = {i : [] for i in range(n)}
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()
        res = 0

        def dfs(node):
            seen.add(node)
            for u in adj[node]:
                if u not in seen:
                    dfs(u)

        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1

        return res