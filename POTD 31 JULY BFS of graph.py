from typing import List
from queue import Queue
from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        visited=[0]*(V)
        queue=deque()
        queue.append(0)
        visited[0]=1
        
        bfs=[]
        while queue:
            node=queue.popleft()
            bfs.append(node)
            for nbr in adj[node]:
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr]=1
        return bfs
