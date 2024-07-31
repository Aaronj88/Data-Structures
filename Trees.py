class Tree_node:
    def __init__(self,value):
        self.data = value
        self.left_node = None
        self.right_node = None

def inorder_traversel(root):
    if root.left_node != None:
            inorder_traversel(root.left_node)
    print(root.data)
    if root.right_node != None:
            inorder_traversel(root.right_node)
    
def post_order(root):
    if root.left_node != None:
            post_order(root.left_node)
    if root.right_node != None:
            post_order(root.right_node)
    print(root.data)

def pre_order(root):
    print(root.data)
    if root.left_node != None:
            pre_order(root.left_node)
    if root.right_node != None:
            pre_order(root.right_node)



a = Tree_node(0)
a.left_node = Tree_node(1)
a.right_node = Tree_node(2)
a.left_node.left_node = Tree_node(3)
a.right_node.left_node = Tree_node(4)
a.right_node.right_node = Tree_node(5)

pre_order(a)
print(' ')
inorder_traversel(a)
print(' ')
post_order(a)




