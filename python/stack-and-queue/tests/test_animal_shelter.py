from stack_and_queue.animal_shelter import *


def test_happy_path_get_name():
    firstDog = Dog('firstDog')
    new = AnimalShelter()
    new.enqueue(firstDog)
    actual = new.dequeue('dog')
    expected = 'firstDog'
    assert actual == expected

def test_happy_path_enqueue_multi_name():
    firstDog = Dog('firstDog')
    secondDog=Dog('secondDog')
    firstCat = Cat('firstCat')
    new = AnimalShelter()
    new.enqueue(firstDog)
    new.enqueue(secondDog)
    new.enqueue(firstCat)
    actual = new.dequeue('cat')
    expected = 'firstCat'
    assert actual == expected

def test_expected_failure():
    firstDog = Dog('firstDog')
    new = AnimalShelter()
    new.enqueue(firstDog)
    actual = new.dequeue('dog')
    expected = 'second'
    assert actual != expected

def test_return_None():
    new = AnimalShelter()
    firstDog = Dog('firstDog')
    new.enqueue(firstDog)
    actual = new.dequeue('test None')
    expected = None
    assert actual == expected
