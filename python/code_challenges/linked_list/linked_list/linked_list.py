class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              current = self.head
              self.head= node
              self.head.next=current

    def includes(self,num):

          x=False

          current = self.head
          while current:
              if current.value==num:

                  x=True
                  break
              current=current.next
          return x

    def append(self, value):

        new_node=Node(value)
        if self.head is None:
          self.head = new_node
          return
        last = self.head
        while (last.next):
            last = last.next

        last.next =  new_node


    def insert_before(self ,value, new_data):

        current = self.head
        if current.value==value:
            self.insert(new_data)
        else:
          while current:
             if current.next.value==value :
                nextvalue=current.next
                current.next=Node(new_data)
                current.next.next=nextvalue
                break
             current=current.next

    def insert_after(self, value, new_data):

        current = self.head
        while current:

            if current.value==value :
                nextvalue=current.next
                current.next=Node(new_data)
                current.next.next=nextvalue
                break
            current=current.next



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
     after=LinkedList()
     after.append(10)
     after.append(20)
     after.insert_after(10,0)
     print(after.__str__())
