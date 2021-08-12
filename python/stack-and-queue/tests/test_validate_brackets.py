import pytest
from stack_and_queue.validate_brackets import *


def test_validation():
    assert bracket_validation('[]()[]') == True
    assert bracket_validation('{}') == True
    assert bracket_validation('{}(){}') == True
    assert bracket_validation('()[[Extra Characters]]') == True
    assert bracket_validation('(){}[[]]') == True
    assert bracket_validation('{}{Code}[Fellows](())') == True
    assert bracket_validation('[({}]') == False
    assert bracket_validation('(](') == False
    assert bracket_validation('{(})') == False
