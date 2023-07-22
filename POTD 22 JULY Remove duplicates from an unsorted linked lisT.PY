class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        c=head
        p=None
        d={}
        while c:
            if c.data not in d:
                d[c.data]=None
                p=c
            else:
                p.next=c.next
            c=c.next    
        return head
