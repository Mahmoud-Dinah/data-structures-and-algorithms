class Vertex:
    pass

class Edge:
    def __init__(self,vertex, weight=1):
        pass

class Graph:
    def __init__(self):
        self._adjacency_list = {
    }

    def add_vertex(self, vertex: Vertex):
        pass


    def add_edges(self, vertex1, vertex2, weight=1):
        pass


    def get_nodes(self):
        pass

    def get_neighbors(self):
         pass

    def to_adj_list(self):
        return self._adajacency_list

    def _breadthFirst(self, action=lambda x: print(x)):
        pass


if __name__ == "__main__":
    pass
