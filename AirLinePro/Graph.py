from Vertex import VertexClass
from Edge import EdgeClass
class Graph :

    #singleTon graph
    _instance = None
    edges : set
    vertices : set
    #first we append all our vertices in the graph
    def __init__(self):
        # self.edges = list()
        # self.vertices = list()
        #
        # if Graph._instance is None :
        #     Graph._instance = self
        raise RuntimeError('Call instance() instead')


    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            #Creating new instance
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance


    def get_vertex(self , name):
        for vertex in self.vertices :
            if isinstance(vertex , VertexClass) and vertex.name == name:
                return vertex
        return None
    def add_vertex(self , new_vertex):
        self.vertices.append(new_vertex)

    def get_edge(self , starting : VertexClass , ending : VertexClass):
        try:
            if starting.connected_vertices.keys().__contains__(ending):
                return starting.connected_vertices[ending]
        except Exception :
            return None

    def add_edge(self ,starting : VertexClass, ending : VertexClass):
        if self.get_edge(starting , ending) is None:
            edge = EdgeClass(starting , ending)
            starting.connected_vertices[ending] = edge
            ending.connected_vertices[starting] = edge
            self.edges.add(edge)


