class TreeNode(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def insert (self, root, value):
            if not root:
                return TreeNode(value)
            elif value < root.value:
                 root.left = self.insert(root.left, value)
            else:
                 root.right = self.insert(root.right, value)

            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

            balanceFactor = self.getBalanceFactor(root)

            if balanceFactor > 1 and value < root.left.value:
                return self.rightRotate(root)
            
            if balanceFactor > 1 and value > root.left.value:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

            if balanceFactor < -1 and value > root.right.value:
                return self.leftRotate(root)
            
            if balanceFactor < -1 and value < root.right.value:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
            
            return root
    
    def search(self, root, value):
        if root is None or root.value == value:
            return root

        if root.value < value:
            return self.search(root.right, value)

        return self.search(root.left, value)
    
    def delete (self, root, value):
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalanceFactor(root)

        if balanceFactor > 1:
            if self.getBalanceFactor(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalanceFactor(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def getHeight(self, root):
        if not root:
            return 0

        return root.height
    
    def getBalanceFactor(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def rightRotate(self, node):
        
        newNode = node.left
        temp = newNode.right

        newNode.right = node
        node.left = temp

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        newNode.height = 1 + max(self.getHeight(newNode.left), self.getHeight(newNode.right))

        return newNode
    
    def leftRotate(self, node):

        newNode = node.right
        temp = newNode.left

        newNode.left = node
        node.right = temp

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        newNode.height = 1 + max(self.getHeight(newNode.left), self.getHeight(newNode.right))

        return newNode
    
class PrintHelper(object):
    def getCol(self, height):
        if height == 1:
            return 1
        return self.getCol(height-1) + self.getCol(height-1) + 1

    def treeFormatter(self, M, root, col, row, height):
        if root is None:
            return
        M[row][col] = root.value
        self.treeFormatter(M, root.left, col-pow(2, height-2), row+1, height-1)
        self.treeFormatter(M, root.right, col+pow(2, height-2), row+1, height-1)

    def treePrinter(self, root):
        h = root.height
        col = self.getCol(h)    
        M = [[0 for _ in range(col)] for __ in range(h)]
        self.treeFormatter(M, root, col//2, 0, h)

        for i in M:
            for j in i:
                if j == 0:
                    print(" ", end=" ")
                else:
                    print(j, end=" ")
            print("")

Tree = AVLTree()
root = None

data = [1,2,3,4,5,6,8,7,9]

for d in data:
    root = Tree.insert(root, d)
print(f"\nTree after insertion of {data}")
PrintHelper().treePrinter(root)

valueToDelete = 4
root = Tree.delete(root, valueToDelete)
print(f"\nTree after deletion of {valueToDelete}:")
PrintHelper().treePrinter(root)

valueToSearch = 5
nodeFound = Tree.search(root, valueToSearch)
print("\nSearch result:")
if nodeFound is None:
    print("Node not found!")
else:
    print(f"Node: {nodeFound.value}\nLeftNode: {nodeFound.left.value}\nRightNode: {nodeFound.right.value}\nHeight: {nodeFound.height}")