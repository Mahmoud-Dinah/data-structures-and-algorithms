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

class HsahTable:
    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None] * self.size


    def hash(self,key:str) -> int:
        value = 0
        for x in key:
            value += ord(x)
        index = (value * 7) % self.size
        return index

    def add(self,key,value):
        index = self.hash(key)

        if not self ._buckets[index]:
            self ._buckets[index] = LinkedList()

        self._buckets[index].append([key,value])
