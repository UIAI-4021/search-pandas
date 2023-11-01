from Vertex import VertexClass
from Edge import EdgeClass
class Graph :

    #singleTon graph
    _instance = None
    edges : set
    vertices : set
    #first we append all our vertices in the graph
    def __init__(self):

        raise RuntimeError('Call instance() instead')


    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            #Creating new instance
            cls._instance = super(Graph, cls).__new__(cls)

            cls._instance.vertices = set()  #to initialize the vertices and end as the instance variable
            cls._instance.edges = set()

            # Put any initialization here.
        return cls._instance


    def get_vertex(self , name):
        for vertex in self.vertices :
            if isinstance(vertex , VertexClass) and vertex.name == name:
                return vertex
        return None
    def add_vertex(self , new_vertex):
        if not self.vertices.__contains__(new_vertex):
            self.vertices.add(new_vertex)

    def get_edge(self , starting : VertexClass , ending : VertexClass):

        for edge in self.edges:
            if isinstance(edge , EdgeClass) and edge.start == starting and edge.end == ending:
                return edge
        return None

    def add_edge(self ,starting : VertexClass, ending : VertexClass , cost = 0):
        if self.get_edge(starting , ending) is None:
            edge = EdgeClass(starting, ending, cost)
            starting.connected_vertices[ending] = edge
            ending.connected_vertices[starting] = edge
            self.edges.add(edge)


