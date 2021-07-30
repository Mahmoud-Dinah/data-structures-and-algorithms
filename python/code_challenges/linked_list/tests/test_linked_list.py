from linked_list import __version__
from linked_list.linked_list import (
    Node,
    LinkedList,
)

def test_instantiate_empty_linked_list():
    # test 1 -- empty linked list
    new = LinkedList()
    new.insert()
    actual = new.__str__()
    expected='( null ) -> NULL'
    assert actual==expected

def test_insert():
    # test 2 -- insert into linked list
    new = LinkedList()
    new.insert("Mahmoud")
    actual=new.__str__()
    expected='( Mahmoud ) -> NULL'
    assert actual==expected

def test_head_value():
    # test 3 -- test head value
    ahmad = LinkedList()
    ahmad.insert(7)
    actual=ahmad.head.value
    expected= 7
    assert actual==expected

def test_insert_multiple_nodes():
    # test 4 -- insert multiple_nodes
    new = LinkedList()
    new.insert(1)
    new.insert(2)
    new.insert("Mahmoud")
    actual= new.__str__()
    expected='( Mahmoud ) -> ( 2 ) -> ( 1 ) -> NULL'
    assert actual==expected

def test_includes_True():
    # test 5 -- searching a number if it is included in the linked_list
    new = LinkedList()
    new.insert(7)
    new.insert(5)
    new.insert(3)
    new.insert(200)
    actual = new.includes(7)
    expected = True
    assert actual == expected

def test_includes_False():
    # test 6 --  searching for a value in the linked list that does not exist
    new = LinkedList()
    new.insert(7)
    new.insert(5)
    new.insert(3)
    new.insert(200)
    actual = new.includes(740)
    expected = False
    assert actual == expected


def test_return_all_value():
    new =LinkedList()
    new.insert('Mahmoud')
    new.insert('is')
    new.insert('name')
    new.insert('my')
    actual = new.__str__()
    expected = '( my ) -> ( name ) -> ( is ) -> ( Mahmoud ) -> NULL'

    assert actual == expected
