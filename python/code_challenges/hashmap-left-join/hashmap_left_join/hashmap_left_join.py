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
        if self.bucckets[hashKey]:
            self.bucckets[hashKey].head.value[0]
            current=self.bucckets[hashKey].head
            while current:
                if current.value[0] == key:
                    return True
                else:
                    current = current.next
        return False


    def get(self,key):
        hashKey = self.hash(key)
        if self.bucckets[hashKey]:
            self.bucckets[hashKey].head.value[0]
            current=self.bucckets[hashKey].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                else:
                    current =current.next

        return None

def left_join(hash_one,hash_two):
    array = []
    for index in hash_one.bucckets:
        if index:
            array_Two=[]
            array_Two.append(index.head.value[0])
            array_Two.append(hash_one.get(index.head.value[0]))
            array_Two.append(hash_two.get(index.head.value[0]))
            array.append(array_Two)
    return array
if __name__ == "__main__":
    hash_one = HsahTable()
    hash_one.add('test', 'roll')
    hash_one.add('qwe', 'in')
    hash_one.add('test', 'in')
    hash_one.add('color', 'red')
    hash_two = HsahTable()
    hash_two.add('color', 'red')
    hash_two.add('in', 'roll')
    hash_two.add('in', 'in')
    print(left_join(hash_one,hash_two))
