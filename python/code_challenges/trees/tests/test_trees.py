from trees.trees import *

def test_instantiate_an_empty_tree():
    tree = BinarySearchTree()
    treeBinary = BinaryTree()
    assert str(tree) == 'tree instantiate'
    assert str(treeBinary) == 'tree instantiate'
