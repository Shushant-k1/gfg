def findMedian(root):
    # code here
    # return the median
    li=[]
    inorder(li,root)
    #print(li)
    n=len(li)
    if n%2==0:
        s=(li[(n-1)//2]+li[n//2])//2
        t=(li[(n-1)//2]+li[n//2])/2
        if t-s==0.0:
            return s
        else:
            return t
    else:
        return li[len(li)//2]
def inorder(li,root):
    if root==None:
        return
    else:
        inorder(li,root.left)
        li.append(root.data)
        inorder(li,root.right)
        return
