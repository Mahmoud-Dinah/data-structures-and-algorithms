class Node:
    def __init__(self, value):
        self.value = value
        self.children=[]

class K_ary_tree:
    def __init__(self):
        self.root = None


def fizz_buzz_tree(K_ary_tree):

    def traverse(node):
        if node.children:
            for i in range(len(node.children)):
                traverse(node.children[i])
                if node.children[i].value%5==0 and node.children[i].value%3==0:

                    node.children[i].value='Fizz Buzz'
                elif node.children[i].value%5==0:

                    node.children[i].value='Buzz'
                elif node.children[i].value%3==0:

                    node.children[i].value='Fizz'
                else:
                    node.children[i].value=str(node.children[i].value)
    traverse(K_ary_tree.root)
    if K_ary_tree.root.value%5==0 and K_ary_tree.root.value%3==0:

        K_ary_tree.root.value='Fizz Buzz'
    elif K_ary_tree.root.value%5==0:

        K_ary_tree.root.value='Buzz'
    elif K_ary_tree.root.value%3==0:

        K_ary_tree.root.value='Fizz'
    else:
        K_ary_tree.root.value=str(K_ary_tree.root.value)

    return K_ary_tree


if __name__ == "__main__":

    # K_ary_tree = K_ary_tree()
    # K_ary_tree.root=Node(1)
    # K_ary_tree.root.children+=[Node(2)]
    # K_ary_tree.root.children+=[Node(3)]
    # K_ary_tree.root.children+=[Node(4)]
    # K_ary_tree.root.children[0].children+=[Node(5)]
    # K_ary_tree.root.children[0].children+=[Node(6)]
    # K_ary_tree.root.children[0].children+=[Node(7)]
    # K_ary_tree.root.children[1].children+=[Node(8)]
    # K_ary_tree.root.children[2].children+=[Node(9)]
    # K_ary_tree.root.children[2].children+=[Node(10)]
    # K_ary_tree.root.children[0].children[2].children+=[Node(11)]
    # K_ary_tree.root.children[0].children[2].children+=[Node(2)]
    # K_ary_tree.root.children[2].children[1].children+=[Node(13)]
    # K_ary_tree.root.children[2].children[1].children+=[Node(115)]
    # K_ary_tree.root.children[2].children[1].children+=[Node(15)]
    # K_ary_tree.root.children[2].children[1].children+=[Node(16)]

    tree = K_ary_tree()
    tree.root=Node(1)
    tree.root.children+=[Node(2)]
    tree.root.children+=[Node(3)]
    fizz_buzz_tree(tree)
    print(tree.root.children[1].value)

