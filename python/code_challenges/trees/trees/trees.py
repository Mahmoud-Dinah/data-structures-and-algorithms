class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Binary_tree:
    def __init__(self):
        self.root = None


    def pre_order(self):
        output = ""
        if not self.root:
            return 'emoty tree'

        def traversals(node):
            nonlocal output
            output += str(node.value)

            if node.left:
                traversals(node.left)

            if node.right:
                traverse(node.right)

        traversals(self.root)
        return output


