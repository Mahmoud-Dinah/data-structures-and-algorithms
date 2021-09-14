from graph_depth_first.graph_depth_first import *


def test_happy_path():
    graph = Graph()
    a= graph.add_vertix('a')
    b= graph.add_vertix('b')
    c= graph.add_vertix('c')
    d= graph.add_vertix('d')
    e= graph.add_vertix('e')
    f= graph.add_vertix('f')
    g= graph.add_vertix('g')
    h= graph.add_vertix('h')
    graph.add_edges(a,b)
    graph.add_edges(a,d)
    graph.add_edges(b,a)
    graph.add_edges(b,c)
    graph.add_edges(b,d)
    graph.add_edges(c,b)
    graph.add_edges(c,g)
    graph.add_edges(g,c)
    graph.add_edges(d,a)
    graph.add_edges(d,b)
    graph.add_edges(d,e)
    graph.add_edges(d,h)
    graph.add_edges(d,f)
    graph.add_edges(e,d)
    graph.add_edges(f,d)
    graph.add_edges(f,h)
    graph.add_edges(h,d)
    graph.add_edges(h,f)
    assert graph.depth_first(a) == [a, b, c, g, d, e, h, f]


def test_edge():
    graph = Graph()
    test=Vertix('test')
    assert graph.depth_first(test)== ' no such path in selected root'
