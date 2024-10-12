class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        

newBT = TreeNode("Drinks")
leftchild = TreeNode("Hot")
rightchild = TreeNode("Cold")
newBT.leftchild = leftchild
newBT.rightchild = rightchild




def PreOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    PreOrderTraversal(rootNode.leftchild)
    PreOrderTraversal(rootNode.rightchild)
    
PreOrderTraversal(newBT)
print("*" * 50)



def InOrderTraversal(rootNode):
    if not rootNode:
        return
    InOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    InOrderTraversal(rootNode.rightchild)
    
InOrderTraversal(newBT)
print("*" * 50)




def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftchild)
    PostOrderTraversal(rootNode.rightchild)
    print(rootNode.data)
    
PostOrderTraversal(newBT)
print("*" * 50)
    




