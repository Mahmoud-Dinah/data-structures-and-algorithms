from linked_list_zip.linked_list_zip import LinkedList

def test_zip_two_list():
    first_list = LinkedList()
    second_list = LinkedList()
    first_list.insert(13)
    first_list.insert(3)
    first_list.insert(11)
    second_list.insert(7)
    second_list.insert(4)
    second_list.insert(22)
    first_list.zip_lists(a=first_list, b=second_list)
    actual = first_list.__str__()
    expected = '( 11 ) -> ( 22 ) -> ( 3 ) -> ( 4 ) -> ( 13 ) -> ( 7 ) -> None'
    assert actual == expected

def test_two_is_empty():
    first_list = LinkedList()
    second_list = LinkedList()
    first_list.zip_lists(a=first_list, b=second_list)
    actual = first_list.__str__()
    expected = ''
    assert actual == expected


def test_one_list_is_empty():
    first_list = LinkedList()
    second_list = LinkedList()
    first_list.insert(7)
    first_list.insert(8)
    first_list.insert(9)
    first_list.insert(10)
    first_list.zip_lists(a=first_list, b=second_list)
    actual = first_list.__str__()
    expected = '( 10 ) -> ( 9 ) -> ( 8 ) -> ( 7 ) -> None'
    assert actual == expected
