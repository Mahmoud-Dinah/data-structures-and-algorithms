import re

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

def repeated_word(words:str):
        if words == None:
            return 'Not found'
        hashed = HsahTable()

        words = re.sub('\W+', ' ', words).lower().split()

        for word in words:
            if hashed.contains(word):
                return word
            else:
                hashed.add(word,True)

if __name__ == "__main__":
    words = "Once upon a time, there was a brave princess who..."
    wordsTwo = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

    print (repeated_word(words))
    print (repeated_word(wordsTwo))
