from _typeshed import Self


class Node:
  def __init__(self,value):
      self.value = value
      self.next = None

class Stack:
    Self.top = None


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


