class Tree:

    def __init__ (self,data):
        self.data = data
        self.l_child = None
        self.r_child = None


def Insert(root,x):
    if root == None:
        return Tree(x)
    if root.data > x:
        root.l_Child = Insert(root.l_child,x)
    else:
        root.r_child = Insert(root.r_child,x)
    return root

def Search(root,key):
    if root.data == key:
        return root
    elif root.data > key and root.l_child != None:
        return Search(root.l_child,key)
    elif root.data < key and root.r_child != None:
        return Search(root.r_child,key)
    else:
        return -1


def inorder(root):
    if root.l_child != None:
        inorder(root.l_child)
    print(root.data)
    if root.r_child != None:
        inorder(root.r_child)


n = int(input('Enter the amount of elements you would like in your tree:    '))
root = None
for i in range(n):
    x = int(input('Enter the value you would like to assign to your node:   '))
    root = Insert(root,x)

inorder(root)

key = int(input("Enter the value of the node you would like to search for:    "))
keyNode = Search(root,key)

if keyNode == -1:
    print("This node is not in your tree.")
else:
    print("This node was found in your tree", keyNode.data)




