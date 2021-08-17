from trees.tree_fizz_buzz import *


def test_tree_fizz_buzz_values():
    tree = K_ary_tree()
    tree.root=Node(1)
    tree.root.children+=[Node(2)]
    tree.root.children+=[Node(3)]
    fizz_buzz_tree(tree)
    assert tree.root.children[1].value == 'Fizz'
