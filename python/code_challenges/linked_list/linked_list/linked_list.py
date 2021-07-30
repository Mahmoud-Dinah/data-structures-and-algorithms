class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):
        try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current
        except Exception as e:
          raise Exception(f"error happend : {e}")

    def includes(self,num):
        try:
          x=False

          current = self.head
          while current:
              if current.value==num:

                  x=True
                  break
              current=current.next
          return x
        except Exception as e:
          raise Exception(f"error happend : {e}")



    def __str__(self):
        output = ""
        current = self.head
        while current:
            value = current.value
            if current.next is None:
                output += f"( {value} ) -> NULL"
                break
            output += f"( {value} ) -> "
            current=current.next
        return output

if __name__ == "__main__":
    new =LinkedList()
    new.insert('Mahmoud')
    new.insert('is')
    new.insert('name')
    new.insert('my')
    actual = new.__str__()
    print(new.__str__())
