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
            output.insert(current.value)
            current = current.next
        return f'{output}'

class HsahTable:
    def __init__(self, size = 1024):
        self.size = size
        self.bucckets = [None] * self.size


    def hash(self,key:str) -> int:
        value = 0
        for x in key:
            value += ord(x)
        index = (value * 7) % self.size
        return index

    def add(self,key,value):
        index = self.hash(key)

        if not self.bucckets[index]:
            self.bucckets[index] = LinkedList()

        self.bucckets[index].insert([key,value])

    def contains(self,key):
        hashKey = self.hash(key)
        if not self.bucckets[hashKey]:
            self.bucckets[hashKey].head.value[0]
            current=self.bucckets[hashKey].head
            while current:
                if current.value[0] != key:
                    return False
                else:
                    current = current.next
        return True


    def get(self,key):
        hashKey = self.hash(key)
        if not self.bucckets[hashKey]:
            self.bucckets[hashKey].head.value[0]
            current=self.bucckets[hashKey].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                else:
                    current =current.next

        return hashKey


if __name__ == '__main__':
    hashtable = HsahTable()
    hashtable.add('test get', 64)

    print(hashtable.get('test get'))
    print(hashtable.contains('test get'))
