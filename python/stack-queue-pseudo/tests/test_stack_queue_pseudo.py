from stack_queue_pseudo.stack_queue_pseudo import *


def test_enqeue_one_value_pseudoqueue():
    new = Pseudo_queue()
    new.enqueue(3)
    actual = (new.front.top.value)
    expected = 3
    assert actual == expected

def test_enqeue_multi_value_pseudoqueue():
    new = Pseudo_queue()
    new.enqueue(3)
    new.enqueue(4)
    new.enqueue(5)
    actual = (new.front.top.value)
    expected = 5
    assert actual == expected

def test_deqeue_multi_value_pseudoqueue():
    new = Pseudo_queue()
    new.enqueue(3)
    new.enqueue(4)
    new.enqueue(5)
    new.dequeue()
    new.dequeue()
    new.dequeue()
    actual = (new.front.top)
    expected = None
    assert actual == expected

def test_empty_pseudoqueue():
    new = Pseudo_queue()
    assert new.front.top == None

