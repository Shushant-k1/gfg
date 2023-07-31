def dfsOfGraph(self, V, adj):
        # code here
        visited = [False] * V
        res = []
        def dfs(at):
            if visited[at]:
                return
            else:
                visited[at] = True
                res.append(at)
                
            nxt_nodes = adj[at]
            
            for nxt in nxt_nodes:
                dfs(nxt)
        
        start_node = 0
        dfs(start_node)
        return res
