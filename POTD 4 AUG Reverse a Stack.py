from typing import List

class Solution:
    
    def reverse(self,St):
        
        def swap(idx,n,St):
            
            if idx > n:
                
                return 
            
            St[idx] , St[n] = St[n] , St[idx]
            
            swap(idx+1,n-1,St)
            
        swap(0,len(St)-1,St)
