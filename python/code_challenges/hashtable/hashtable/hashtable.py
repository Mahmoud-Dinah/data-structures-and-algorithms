class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current

    def __str__(self):
        output = []
        current = self.head
        while current:
            output.append(current.value)
            current = current.next
        return f'{output}'

if __name__ == "__main__":
    new =LinkedList()
    new.insert('Mahmoud')
    new.insert('is')
    new.insert('name')
    new.insert('my')
    new.__str__()
    print(new.__str__())
