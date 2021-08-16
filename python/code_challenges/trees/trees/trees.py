class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self,value):
        node = Node(value)
        if not self.rare:
            self.front = node
            self.rare = node
        else:
            self.rare.next = node
            self.rare = node

    def dequeue(self):
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def is_empty(self):
        return  not (self.front and self.rare)

    def peek(self):
     if self.is_empty():
         raise Exception('empty queue')
     else:
        return self.front.value


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
    def max_value(self):
            max_number=0
            def inner_def(current):
                nonlocal max_number
                if current.value > max_number :
                    max_number = current.value

                if current.left:
                    inner_def(current.left)
                if current.right:
                    inner_def(current.right)

            inner_def(self.root)
            return max_number


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


def breadth_first(tree):
    queue = [tree.root]
    breadth=[]
    if tree.root==None:
        return []

    while queue:

        node=queue[0]
        if node.left != None:
            queue+=[node.left]

        if node.right != None:
            queue+=[node.right]

        breadth+=[queue[0].value]
        queue=queue[1:]
    return breadth

if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    print(breadth_first(tree))
