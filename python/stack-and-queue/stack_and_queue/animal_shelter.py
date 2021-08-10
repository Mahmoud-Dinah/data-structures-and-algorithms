class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

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
        temp.next = None
        return temp.value

    def is_empty(self):
        return  not (self.front and self.rare)

    def peek(self):
     if self.is_empty():
         raise Exception('empty queue')
     else:
        return self.front.value

class Dog:
    def __init__(self,name):
        self.name=name
        self.type='dog'

class Cat:
    def __init__(self,name):
        self.name=name
        self.type='cat'

class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):

        if animal.type=='cat':
            self.cat.enqueue(animal)
        elif animal.type=='dog':
            self.dog.enqueue(animal)
        else:
            return 'only cat or dog allowd'
    def dequeue(self,input=None):
        if input == 'cat':
            return self.cat.dequeue().name
        elif input == 'dog':
            return self.dog.dequeue().name
        else:
            return None
if __name__ == "__main__":
    firstDog = Dog('firstDog')
    secondDog=Dog('secondDog')
    thirdDog=Dog('thirdDog')
    firstCat = Cat('firstCat')
    secondCat = Cat('secondCat')
    new = AnimalShelter()
    new.enqueue(firstDog)
    new.enqueue(secondDog)
    new.enqueue(thirdDog)
    new.enqueue(firstCat)
    print(new.dequeue('dog'))
    print(new.dequeue('dog'))
    print(new.dequeue('cat'))
