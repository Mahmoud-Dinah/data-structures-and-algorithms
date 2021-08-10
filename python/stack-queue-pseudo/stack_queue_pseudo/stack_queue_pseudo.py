class Node:
  def __init__(self,value):
      self.value = value
      self.next = None

class Stack:
    def __init__(self):
      self.top = None


    def push(self,value):
       node = Node(value)
       node.next = self.top
       self.top = node

    def pop(self):
        item = self.top.value
        self.top = self.top.next
        return item

    def peek(self):
        return self.top.value

    def isEmpty(self):
        return self.top==None

class Pseudo_queue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self,value=None):
        self.front.push(value)

    def dequeue(self):

        while self.front.top:
            self.rear.push(self.front.pop())
        dequeueitem = self.rear.pop()
        while self.rear.top:
            self.front.push(self.rear.pop())
        return dequeueitem



def __str__(self):
        current=self.front.top
        new =''
        while current:
            if not current.next:
                new = new +f'( {current.value} )'
                current=current.next
            else:
                new = new +f'( {current.value} ) -> '
                current=current.next
        return new

if __name__ == "__main__":
    new = Pseudo_queue()
    new.enqueue(1)
    new.enqueue(2)
    new.enqueue(3)
    print(new.__str__())
    print(new.front.top.value)
