def reverse(self,head, k):
        # Code here
        cur = head
        cnt = 0
        vals = [[]]
        while cur:
            vals[-1].append(cur.data)
            cnt += 1
            if not cnt % k:
                vals.append([])
                cnt = 0
            cur = cur.next
        vals = [i[::-1][j] for i in vals for j in range(len(i))]
        cur = head
        cnt = 0
        while cur:
            cur.data = vals[cnt]
            cnt += 1
            cur = cur.next
        return head
