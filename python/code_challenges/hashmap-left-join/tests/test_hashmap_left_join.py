from hashmap_left_join.hashmap_left_join import *


def test_happey_path():
    hash_one = HsahTable()
    hash_one.add('test', 'roll')
    hash_one.add('qwe', 'in')
    hash_one.add('test', 'in')
    hash_one.add('color', 'red')
    hash_two = HsahTable()
    hash_two.add('color', 'red')
    hash_two.add('in', 'roll')
    hash_two.add('in', 'in')
    assert (left_join(hash_one,hash_two)) == [['test', 'in', None], ['qwe', 'in', None], ['color', 'red', 'red']]
