from Vertex import VertexClass
from Edge import EdgeClass
class Graph :

    #singleTon graph
    _instance = None
    edges : set
    vertices : set

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


    def add_vertex(self , new_vertex):
        self.vertices.append(new_vertex)

    def add_edge(self ,starting : VertexClass, ending : VertexClass):
        new_edge = EdgeClass(starting , ending , 0)

