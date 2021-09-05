from hashtable.hashtable import *
def test_add():
    hash = HsahTable()
    hash.add('test', 64)
    assert hash.get('test') == 64


def test_get():
    hash = HsahTable()
    hash.add('test get', 480)
    assert hash.get('test get') == 480

def test_contain():
    hash = HsahTable()
    hash.add('test get', 480)
    assert hash.contains('test get') == True
