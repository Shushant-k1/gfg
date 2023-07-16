class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        #add code here
        stack=[]
        while not q.empty():
            stack.append(q.get())
        while len(stack)!=0:
            q.put(stack.pop())
        return q
