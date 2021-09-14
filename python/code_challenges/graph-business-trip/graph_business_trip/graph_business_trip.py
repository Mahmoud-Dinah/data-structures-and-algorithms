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

def business_trip(graph,cities):
        cost = 0
        fly = True
        for i in range(len(cities)-1):
            for city in graph.get_neighbors(cities[i]):
                if cities[i+1] == city[0]:
                    cost+=city[1]
                    break
            else:
                fly = False
        if fly==False:
            cost=0

        return fly, f'${cost}'


if __name__ == "__main__":
    graph = Graph()

    New_Monstropolis= graph.add_vertix('New Monstropolis')
    pandora= graph.add_vertix('pandora')
    naboo= graph.add_vertix('naboo')
    metroville= graph.add_vertix('metroville')
    narina= graph.add_vertix('narina')
    arendelle= graph.add_vertix('arendelle')
    manstropolis= graph.add_vertix('manstropolis')
    graph.add_edges(pandora,metroville,82)
    graph.add_edges(arendelle,metroville,99)
    graph.add_edges(metroville,manstropolis,105)
    graph.add_edges(arendelle,manstropolis,42)
    graph.add_edges(metroville,pandora,82)
    graph.add_edges(arendelle,pandora,150)
    graph.add_edges(pandora,arendelle,150)
    graph.add_edges(metroville,arendelle,99)
    graph.add_edges(metroville,narina,37)
    graph.add_edges(narina,metroville,37)
    graph.add_edges(naboo,manstropolis,73)
    graph.add_edges(naboo,narina,250)
    graph.add_edges(naboo,metroville,26)
    graph.add_edges(metroville,naboo,26)
    graph.add_edges(manstropolis,naboo,73)
    graph.add_edges(narina,naboo,250)
    graph.add_edges(manstropolis,arendelle,42)
    graph.add_edges(manstropolis,metroville,105)
    print(business_trip(graph,[metroville,narina]))
