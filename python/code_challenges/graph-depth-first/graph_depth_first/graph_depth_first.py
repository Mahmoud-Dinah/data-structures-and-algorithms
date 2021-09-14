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

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():
            output += vertix.value
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value
                output += '\n'
        return output

    def depth_first(self,start_point):
        if start_point not in self.adjacency_list.keys():
            return ' no such path in selected root'


        value = []
        def recursive(node):
            if not node in value:
                value.append(node)
            for nodes in self.get_neighbors(node):
                if not nodes[0] in value:
                    recursive(nodes[0])

        recursive(start_point)
        return value

if __name__ == "__main__":
    graph = Graph()
    a= graph.add_vertix('1')
    b= graph.add_vertix('2')
    c= graph.add_vertix('3')
    graph.add_edges(a,b)
    graph.add_edges(b,a)
    graph.add_edges(b,c)
    # print(graph.depth_first(a)[0])
    print(graph.depth_first(a))


    graph1 = Graph()
    test=Vertix('test')
    print(graph.depth_first(test))
