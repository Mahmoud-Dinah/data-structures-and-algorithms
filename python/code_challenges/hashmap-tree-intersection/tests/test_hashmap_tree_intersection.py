from hashmap_tree_intersection.hashmap_tree_intersection import *

def test_happy_path():
    first_tree=Binary_tree()
    first_tree.root=NodeNew(1)
    first_tree.root.left=NodeNew(2)
    first_tree.root.right=NodeNew(2)

    sec_tree=Binary_tree()
    sec_tree.root=NodeNew(3)
    sec_tree.root.left=NodeNew(2)
    sec_tree.root.right=NodeNew(1)
    sec_tree.root.left.left=NodeNew(22)
    assert tree_intersection(first_tree,sec_tree) == [2,2,1]
