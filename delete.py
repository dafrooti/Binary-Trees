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
    # return root.value
    return root

def delete(root, key):
    if root == None:
        return None
    if key < root.value:
        root.left = delete(root.left, key)
    elif key > root.value:
        root.right = delete(root.right, key)
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp
        
        # if the root has 2 children
        temp = mostleft(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
    return root

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
    print("Press 2 to search for values")
    print("Press 3 for inorder traversal")
    print("Press 4 for preorder traversal")
    print("Press 5 for postorder traversal")
    print("Press 6 to delete the node of your choice")
    print("Press 7 to exit")

    choice = (input("Enter option: "))

    if choice == "1":
        n = int(input("What number of nodes do you want: "))
        for i in range(n):
            k = int(input("Insert the number for each node: "))
            root = insert(root, k)

    if choice == "1.5":
        print(mostleft(root).value) # is the minimum value

    if choice == "2":
        find = search(root, int(input("What number are you searching for: ")))
        if find == -1:
            print("Not Found")
        else:
            print("Key is found", find.value)
        
    elif choice == "3":
        inorder_traversal(root)
    elif choice == "4":
        preorder_traversal(root)
    elif choice == "5":
        postorder_traversal(root)
    elif choice == "6":
        delete(root, int(input("Type the node to delete: ")))

    elif choice >= "7":
        break