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




if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.pop()
    stack.pop()
    stack.pop()

    # stack.peek()
    print(stack.top.value)
