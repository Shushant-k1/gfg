from collections import deque

class Solution:
    def rightView(self, root):
        ans = []
        if not root:
            return ans
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            counter = 0
            while counter < size - 1:
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                counter += 1
            ans.append(q[0].data)
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q.popleft()
        return ans
