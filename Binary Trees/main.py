class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def display(self):
        print(self.value, self.left, self.right)

def insert(root, k):
    if root == None:
        return Tree(k)
    if root.value > k:
        root.left = insert(root.left, k)
    else:
        root.right = insert(root.right, k)
    return root

def search(root, key):
    if root.value == key:
        return root
    elif root.value > key and root.left is not None:
        return search(root.left, key)
    elif root.value < key and root.right is not None:
        return search(root.right, key)
    else:
        return -1

def mostleft(root):
    # if root is None:

    if root == None:
        return None
    while root.left:
        root = root.left
    return root.value

def mostright(root):
    if root == None:
        return None
    while root.right:
        root = root.right
    return root.value

def inorder_traversal(root):
    if root.left != None:
        inorder_traversal(root.left)
    print(root.value)
    if root.right != None:
        inorder_traversal(root.right)

def preorder_traversal(root):
    print(root.value)
    if root.left != None:
        preorder_traversal(root.left)
    if root.right != None:
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root.left != None:
        postorder_traversal(root.left)
    if root.right != None:
        postorder_traversal(root.right)
    print(root.value)

root = None


while True:
    print("Press 1 to make the nodes")
    print("Press 1.5 for the smallest value")
    print("Press 2 for the largest value")
    print("Press 3 to search for values")
    print("Press 4 for inorder traversal")
    print("Press 5 for preorder traversal")
    print("Press 6 for postorder traversal")
    print("Press 7 to exit")

    choice = (input("Enter option: "))

    if choice == "1":
        n = int(input("What number of nodes do you want: "))
        for i in range(n):
            k = int(input("Insert the number for each node: "))
            root = insert(root, k)

    if choice == "1.5":
        print(mostleft(root))
        
    if choice == "2":
        print(mostright(root))

    if choice == "3":
        find = search(root, int(input("What number are you searching for: ")))
        if find == -1:
            print("Not Found")
        else:
            print("Key is found", find.value)
        
    elif choice == "4":
        inorder_traversal(root)
    elif choice == "5":
        preorder_traversal(root)
    elif choice == "6":
        postorder_traversal(root)

    elif choice >= "7":
        break
