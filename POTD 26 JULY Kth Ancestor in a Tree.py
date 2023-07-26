def kthAncestor(root,k, node):
    #code here
    ans=[]
    def trav(root,su):
        if(root==None):
            return
        if(root.data==node):
            ans.append(su+[root.data])
            return
        trav(root.left,su+[root.data])
        trav(root.right,su+[root.data])
    trav(root,[])
    # print(ans)
    a1=ans[0][::-1]
    if((len(a1)-1)<k):
        return -1
    if((len(a1)-1)>=k):
        return(a1[k])

