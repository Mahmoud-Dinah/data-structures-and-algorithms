class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def zip_lists(self, a, b):
        first = a.head
        second = b.head

        while first != None and second != None:
            fnext = first.next
            snext = second.next
            second.next = fnext
            first.next = second
            first = fnext
            second = snext
            b.head = second
    def __str__(self):
        output = ""
        new = self.head
        while new:
            data = new.data
            if new.next is None:
                output += f"( {data} ) -> None"
                break
            output = output + f"( {data} ) -> "
            new = new.next
        return output

if __name__ == "__main__":
    first_list = LinkedList()
    second_list = LinkedList()
    first_list.insert(12)
    first_list.insert(4)
    first_list.insert(1)
    second_list.insert(22)
    second_list.insert(3)
    second_list.insert(2)
    first_list.zip_lists(a=first_list, b=second_list)
    print(first_list.__str__())
