class Vertix:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self,vertix, weight=1):
        self.vertix = vertix
        self.weight = weight

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertix(self, value):
        v =  Vertix(value)
        self.adjacency_list[v] = []
        return v


    def add_edges(self, vertix_first, vertix_end, weight=1):
        nodes = self.adjacency_list.keys()
        if not vertix_first in nodes and not vertix_end in nodes:
             return 'vertix not in the graph'

        elif not vertix_first in nodes:
            return ' first vertix are not in the graph'

        elif not vertix_end in nodes:
            return 'next vertix is not the graph'

        edge = Edge(vertix_end,weight)
        self.adjacency_list[vertix_first].append(edge)


    def get_nodes(self):
        array = []
        for vertix in self.adjacency_list.keys():
            array.append(vertix)
        if len(array) == 0:
            return None
        return array

    def get_neighbors(self):
         pass

    def to_adj_list(self):
        return self.adjacency_list

    def _breadthFirst(self, action=lambda x: print(x)):
        pass


if __name__ == "__main__":
    graph = Graph()
    a = graph.add_vertix('a')
    b = graph.add_vertix('b')
    graph.add_edges(a, b)
    print(graph.get_nodes())
    print(graph.adjacency_list)
