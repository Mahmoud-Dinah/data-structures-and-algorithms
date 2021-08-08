class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,node=None):
        self.top = node

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def is_empty(self):
        return not self.top

    def peek(self):
        if self.is_empty():
            raise Exception("called on empty stack")
        return self.top.value

class Queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self,value):
        node = Node(value)
        if not self.rare:
            self.front = node
            self.rare = node
        else:
            self.rare.next = node
            self.rare = node

    def dequeue(self):
        temp = self.front
        self.front = self.front.next
        self.rare = self.rare.next
        temp.next = None
        return temp.value

    def is_empty(self):
        return  not (self.front and self.rare)

    def peek():
        pass




if __name__ == "__main__":
#######################################
############ Stack testing ############
#######################################
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.pop()
    # stack.pop()
    # # stack.pop()
    # # stack.peek()
    # print(stack.top.value)

#######################################
############ Queue testing ############
#######################################
    queue = Queue()
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # print(queue.front.value)
    # print(queue.rare.value)
    # print(queue.is_empty())

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue.front.value)
    print(queue.rare.value)
