from typing import Hashable


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

class NodeNew:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self):
        self.root = None

def tree_intersection(first_tree,sec_tree):
    hashed= HsahTable()
    array =[]
    def travers(node):
        if hashed.contains(str(node.value)):
            nonlocal array
            array = array + [node.value]
        else:
            hashed.add(str(node.value),True)

        if node.left:
            travers(node.left)
        if node.right:
            travers(node.right)

    travers(first_tree.root)
    travers(sec_tree.root)

    return array

if __name__ == "__main__":
    first_tree=Binary_tree()
    first_tree.root=NodeNew(150)
    first_tree.root.left=NodeNew(100)
    first_tree.root.right=NodeNew(250)

    sec_tree=Binary_tree()
    sec_tree.root=NodeNew(42)
    sec_tree.root.left=NodeNew(100)
    sec_tree.root.right=NodeNew(600)
    sec_tree.root.left.left=NodeNew(15)
    print(tree_intersection(first_tree,sec_tree))
