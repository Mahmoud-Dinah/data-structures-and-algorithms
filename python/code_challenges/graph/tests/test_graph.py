from graph.graph import *


def test_add_vertix():
    graph = Graph()
    actual = graph.add_vertix('first')
    expected=graph.get_nodes()[0]
    assert actual==expected

def test_add_edges():
    graph = Graph()
    first = graph.add_vertix('first')
    second = graph.add_vertix('second')
    graph.add_edges(first,second)
    actual = graph.get_neighbors(first)[0][0]
    expected = second
    assert actual==expected

def test_get_nodes():
    graph = Graph()
    first = graph.add_vertix('first')
    second = graph.add_vertix('second')
    third = graph.add_vertix('third')
    actual = graph.get_nodes()
    expected = [first,second,third]
    assert actual==expected

def test_get_neighbors_node():
    graph = Graph()
    first = graph.add_vertix('first')
    second = graph.add_vertix('first neighbors')
    graph.add_edges(first,second)
    actual = graph.get_neighbors(first)[0][0]
    expected = second
    assert actual==expected

def test_get_size():
    graph = Graph()
    first = graph.add_vertix('first')
    second = graph.add_vertix('second')
    third = graph.add_vertix('third')
    actual = graph.size()
    expected = 3
    assert actual==expected
