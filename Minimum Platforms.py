class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        z = []
        for i , j in zip(arr,dep) :
            z.append([i , "A"])
            z.append([j , "D"])
        z.sort()
        z.sort(key = lambda x : x[0])
        ans = 0
        mx = 0
        for i in z :
            if i[1] == "A" :
                ans += 1
            else :
                ans -= 1
            mx = max(ans , mx)
        return mx
