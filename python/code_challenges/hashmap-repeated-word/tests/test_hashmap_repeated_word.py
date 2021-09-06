from hashmap_repeated_word.hashmap_repeated_word import *

def test_happy_path():
    words = "Once upon a time, there was a brave princess who..."
    assert repeated_word(words) == 'a'

def test_happy_path_v2():
    words = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert repeated_word(words) == 'summer'

def test_edge_case():
    words = " "
    assert repeated_word(words) == None
