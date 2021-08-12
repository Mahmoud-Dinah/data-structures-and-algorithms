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


