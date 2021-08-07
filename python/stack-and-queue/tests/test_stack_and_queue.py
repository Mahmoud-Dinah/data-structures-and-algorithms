import pytest
from stack_and_queue.stack_and_queue import Node, Stack

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

def test_exp():
    with pytest.raises(Exception):
     stack = Stack()
     stack.push(2)
     stack.push(3)
     stack.pop()
     stack.pop()
     assert stack.peek() == "called on empty stack"

