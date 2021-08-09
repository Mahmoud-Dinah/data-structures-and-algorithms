import pytest
from stack_and_queue.stack_and_queue import *

def test_push_one_value():
    stack = Stack()
    stack.push(2)
    assert stack.top.value == 2

def test_push_multiple_values():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.value == 3

def test_pop_off_the_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.pop()
    stack.pop()
    assert stack.top.value == 1

def test_empty_after_multiple_pops():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.top == None

def test_is_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True

def test_peek_the_next_item_on_the_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    assert stack.peek() == 1

def test_stack_exception():
    with pytest.raises(Exception):
     stack = Stack()
     stack.push(2)
     stack.push(3)
     stack.pop()
     stack.pop()
     assert stack.peek()

def test_queue_into_queue():
     queue = Queue()
     queue.enqueue(1)
     assert queue.front.value == 1
     assert queue.rare.value == 1

def test_multiple_enqueue_into_queue():
     queue = Queue()
     queue.enqueue(1)
     queue.enqueue(2)
     queue.enqueue(3)
     assert queue.front.value == 1
     assert queue.rare.value == 3

def test_dequeue_out_of_queue():
     queue = Queue()
     queue.enqueue(1)
     queue.dequeue()
     assert queue.front == None


def test_peek_into_a_queue():
     queue = Queue()
     queue.enqueue(1)
     assert queue.peek() == 1


def test_empty_queue_after_dequeues():
     queue = Queue()
     queue.enqueue(1)
     queue.enqueue(2)
     queue.enqueue(3)
     queue.dequeue()
     queue.dequeue()
     queue.dequeue()

     assert queue.front == None


def test_instantiate_empty_queue():
    queue = Queue()
    assert queue.is_empty() == True


def test_peek_into_a_empty_queue_raise_expection():
    with pytest.raises(Exception):
     queue = Queue()
     assert queue.peek() == True
