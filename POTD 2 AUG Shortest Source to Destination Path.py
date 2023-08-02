#User function Template for python3

class Solution:
        def shortestDistance(self,N,M,A,X,Y):
            if A[0][0] == 0:
                return -1
    
            ans = -1
            queue = [(0,0,0)]
            while queue :
                (i,j,level) = queue.pop(0)
    
                if (i,j) == (X,Y):
                    ans = level
                    break
    
                for dx in (-1,1):
                    u = i+dx
                    v = j
                    if 0<=u<N and A[u][v] == 1:
                        queue.append((u,v,level+1))
                        A[u][v] = 0
    
                for dy in (-1,1):
                    u = i
                    v = j+dy
                    if 0<=v<M and A[u][v] == 1:
                        queue.append((u,v,level+1))
                        A[u][v] = 0
            return ans
