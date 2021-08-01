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
    # test 7 -- test return all value
    new =LinkedList()
    new.insert('Mahmoud')
    new.insert('is')
    new.insert('name')
    new.insert('my')
    actual = new.__str__()
    expected = '( my ) -> ( name ) -> ( is ) -> ( Mahmoud ) -> NULL'

    assert actual == expected

def test_append_to_the_end_of_a_linked_list():

    append_value=LinkedList()
    append_value.append(1)
    append_value.append(2)
    append_value.append(3)
    actual=append_value.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> NULL'

    assert actual==expected

def test_before_linked_list():
    test_before=LinkedList()
    test_before.append(10)
    test_before.append(20)
    test_before.append(30)
    test_before.insert_before(10,2)
    actual=test_before.__str__()
    expected='( 2 ) -> ( 10 ) -> ( 20 ) -> ( 30 ) -> NULL'
    assert actual==expected

def test_before_the_first_node():
     before=LinkedList()
     before.append(50)
     before.append(60)
     before.insert_before(50,1)
     actual=before.__str__()
     expected='( 1 ) -> ( 50 ) -> ( 60 ) -> NULL'
     assert actual==expected


def test_insert_after():
     after=LinkedList()
     after.append(10)
     after.append(20)
     after.insert_after(10,0)
     actual=after.__str__()
     expected='( 10 ) -> ( 0 ) -> ( 20 ) -> NULL'
     assert actual==expected

def test_insert_after_last_node():
    new=LinkedList()
    new.append(600)
    new.append(700)
    new.insert_after(700,800)
    actual=new.__str__()
    expected='( 600 ) -> ( 700 ) -> ( 800 ) -> NULL'
    assert actual==expected
