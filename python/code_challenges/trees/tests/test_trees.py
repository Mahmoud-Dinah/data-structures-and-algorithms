from trees.trees import *

def test_instantiate_an_empty_tree():
    tree = BinarySearchTree()
    treeBinary = BinaryTree()
    assert str(tree) == 'tree instantiate'
    assert str(treeBinary) == 'tree instantiate'

def test_single_root_node():
    tree = BinarySearchTree()
    tree.Add(2)
    assert tree.root.value == 2

def test_add_left_child_and_right_child_to_single_root_node():
    tree = BinarySearchTree()
    tree.Add(2)
    tree.Add(3)
    tree.Add(1)
    assert tree.root.value == 2
    assert tree.root.left.value == 1
    assert tree.root.right.value == 3

def test_return_collection_from_traversal():
    tree = BinarySearchTree()
    tree.Add(1)
    tree.Add(2)
    tree.Add(3)
    assert tree.print_tree("preorder") == "1  2  3  "
    assert tree.print_tree("inorder") == "1  2  3  "
    assert tree.print_tree("postorder") == "3  2  1  "
