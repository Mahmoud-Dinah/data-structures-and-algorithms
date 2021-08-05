from linked_list.linked_list import (
    Node,
    LinkedList,
)

def list_zip(list1, list2):
    # list1=[]
    # list2=[]
    current1 = list1.head
    current2 = list2.head

    if current1 == None or current2 == None:
        if current1:
            return list1.__str__()
        elif current2:
            return list2.__str__()
        else:
         return "empty list"

    newList = []
    while current1 or current2:
        if(current1):
            newList+=[current1.value]
            current1 = current1.next
        if(current2):
            newList+=[current2.value]
            current2 = current2.next
    n=''
    for i in newList:
      n+=f'( {i} ) -> '
    n+='None'
    return n


list1=LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list2=LinkedList()
list2.append(2)
list2.append(4)
list2.append(7)
list3=LinkedList()
print(list_zip(list1, list2))


##### tests for list zip ######

def test_list_zip_working():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    actual=list_zip(ll1, ll2)
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> ( 5 ) -> ( 6 ) -> None'

    assert actual==expected
