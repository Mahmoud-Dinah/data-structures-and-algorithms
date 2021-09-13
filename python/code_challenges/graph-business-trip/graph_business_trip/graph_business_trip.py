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

    def get_neighbors(self,node):
        array = []
        if node in self.adjacency_list :
             for edge in self.adjacency_list[node]:
                 array.append((edge.vertix, edge.weight))
             return array

    def size(self):
        return len(self.adjacency_list.keys())

    def business_trip(graph,route_map):
        for i in range(len(route_map)-1):
            pass

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            output += vertix.value
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value
                output += '\n'
        return output


if __name__ == "__main__":
    pass
