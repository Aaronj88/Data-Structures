class Tree_node:
    def __init__(self,data):
        self.data = data
        self.r_child = None
        self.l_child = None



def inorder_traversel(root):
    if root.l_child != None:
            inorder_traversel(root.l_child)
    print(root.data)
    if root.r_child != None:
            inorder_traversel(root.r_child)


def Search(root,key):
    if root.data == key:
        return root
    elif root.data > key and root.l_child != None:
        return Search(root.l_child,key)
    elif root.data < key and root.r_child != None:
        return Search(root.r_child,key)
    else:
        return -1


def Insert(root,x):
    if root == None:
        return Tree_node(x)
    if root.data > x:
        root.l_child = Insert(root.l_child,x)
    else:
        root.r_child = Insert(root.r_child,x)
    return root


def Inorder_Successor(root):
    current = root
    while current.l_child != None:
        current = current.l_child
    
    return current

def Delete(root,key):
    if root == None:
        return root
    if key < root.data:
        root.l_child = Delete(root.l_child,key)
    elif key > root.data:
        root.r_child = Delete(root.r_child,key)
    else:
        if root.l_child == None:
            temp = root.l_child
            root = None
            return temp
        elif root.r_child == None:
            temp = root.r_child
            root = None
            return temp
        
        temp = Inorder_Successor(root)
        root.data = temp.data
        root.r_child = Delete(root.r_child,temp.data)



amount = int(input('How many nodes would you like in your tree?     '))
root = None
for i in range(amount):
    value = int(input('What value would you like to assign to your node?    '))
    root = Insert(root,value)

while True:
    print(' ')
    print('Would you like to:')
    print('     1. Insert a new node')
    print('     2. Delete a old node')
    print('     3. Search for a existing node')
    print('     4. See what nodes your tree already contains')

    choice = int(input(' '))


    if choice == 1:
        print(' ')
        value = int(input('What node would you like to insert in your tree?    '))
        root = Insert(root,value)

    elif choice == 2:
        print(' ')
        d_value = int(input('What value would you like to delete?   '))
        Delete(root,d_value)

    elif choice == 3:
        print(' ')
        key = int(input("Enter the value of the node you would like to search for:    "))
        keyNode = Search(root,key)

        if keyNode == -1:
            print(' ')
            print("This node is not in your tree.")
        else:
            print(' ')
            print("The node",keyNode.data,"was found in your tree")

    elif choice == 4:
        inorder_traversel(root)

    else:
        print(' ')
        print('Please enter one of the given options!')








