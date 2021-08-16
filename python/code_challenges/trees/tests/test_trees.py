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

def test_max_value():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(50)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(96)
    tree.root.left.right.left = Node(3)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(2)
    tree.root.right.right = Node(1)
    assert tree.max_value() ==  96

def test_breadthFirst_result():
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
    assert breadth_first(tree) == [2, 7, 5, 2, 6, 9, 5, 11, 4]
