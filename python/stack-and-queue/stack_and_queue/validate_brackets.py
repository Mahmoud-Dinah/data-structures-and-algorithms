from stack_and_queue.stack_and_queue import Stack
from stack_and_queue import *


def left_bracket(bracket):
    if bracket == '(' or bracket =='[' or bracket == '{':
        return True
    else:
        return False

def right_bracket(bracket):
    if bracket == ')' or bracket == ']' or bracket == '}':
        return True
    else:
        return False

def opposite(bracket):
    if bracket == ')':
        return '('
    elif bracket == ']':
        return '['
    elif bracket == '}':
        return '{'

def bracket_validation(input):
    bracket_stack = Stack()

    for i in input:
        if left_bracket(i):
            bracket_stack.push(i)
        if right_bracket(i):
            if bracket_stack.is_empty():
                return False
            else:
                if bracket_stack.top is not None:
                    if opposite(i) == bracket_stack.top.value:
                        bracket_stack.pop()

                    else:
                        return False
                else:
                    return True
    if bracket_stack.is_empty:
        return True



if __name__ == "__main__":
    print(bracket_validation('{}'))
    print(bracket_validation('{}(){}'))
    print(bracket_validation('{}(){}'))
    print(bracket_validation('()[[Extra Characters]]'))
    print(bracket_validation('(){}[[]]'))
    print(bracket_validation('{}{Code}[Fellows](())'))
    print(bracket_validation('[({}]'))
    print(bracket_validation('(]('))
    print(bracket_validation('{(})'))
