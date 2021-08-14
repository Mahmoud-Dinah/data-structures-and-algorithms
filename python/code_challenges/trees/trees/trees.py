class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return "tree instantiate"

    def print_tree(self, traversal):
        if traversal == "preorder":
            return self.pre_order(self.root, "")
        elif traversal == "inorder":
            return self.in_order(self.root, "")
        elif traversal == "postorder":
            return self.post_order(self.root, "")
        else:
            print(str(traversal) + " is not supported.")
            return False

    def pre_order(self, start ,output):
            if start:
                output += f"{str(start.value)}  "
                output = self.pre_order(start.left,output)
                output = self.pre_order(start.right,output)
            return output

    def in_order(self, start ,output):
            if start:
                output = self.in_order(start.left,output)
                output += f"{str(start.value)}  "
                output = self.in_order(start.right,output)
            return output

    def post_order(self, start ,output):
            if start:
                output = self.post_order(start.left,output)
                output = self.post_order(start.right,output)
                output += f"{str(start.value)}  "
            return output

    def array_of_the_values(self):
            max=0
            def inner_def(current):
                nonlocal max
                if current.value > max :
                    max = current.value

                if current.left:
                    inner_def(current.left)
                if current.right:
                    inner_def(current.right)

            inner_def(self.root)
            return max

class BinarySearchTree(BinaryTree):
    def Add(self,value):
            if self.root == None:
                self.root = Node(value)
            global current
            current = self.root
            while current :
                if value == current.value:
                    print("value exisit")
                    return True
                if value > current.value:
                    temp = current
                    current = current.right
                    if current == None:
                        temp.right = Node(value)
                        break
                if value < current.value:
                    temp = current
                    current = current.left
                    if current == None:
                        temp.left = Node(value)
                        break

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(3)
    tree.root.left.right.left = Node(4)
    tree.root.left.right.right = Node(12)
    tree.root.right = Node(2)
    tree.root.right.right = Node(1)
    tree.root.right.right.right = Node(2)
    tree.root.right.right.left = Node(5)
    tree.root.right.right.left.left = Node(8)
    tree.root.left.right.right.right = Node(4)
    print(tree.root.left.value)
    print(tree.print_tree("preorder"))
    print(tree.print_tree("length"))

