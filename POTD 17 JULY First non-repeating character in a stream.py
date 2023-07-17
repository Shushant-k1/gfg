class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        s = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for i in s:
            d[i] = 0
        
        ans = ""
        q = []
        for i in A:
            d[i] += 1
            if d[i]==1:
                q.append(i)
            elif q and q[0] == i:
                q.pop(0)
            for x in q:
                if d[x]==1:
                    ans += x
                    break
            else:
                ans += "#"
        return ans
