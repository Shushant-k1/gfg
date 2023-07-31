class Solution:
    def __init__(self):
        self.l=[]
   
    def dfsOfGraph(self, V, adj):
        visited=[0 for i in range(V)]
        
        self.ccc(V,adj,visited,0)
        return self.l
    def ccc(self,V,adj,visited,k):
        visited[k]=1
        self.l.append(k)
        for i in adj[k]:
            if visited[i]==0:
                self.ccc(V,adj,visited,i)
