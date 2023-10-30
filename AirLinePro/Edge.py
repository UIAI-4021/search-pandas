
from Vertex import VertexClass

class EdgeClass:

    def __init__(self , start : VertexClass, end : VertexClass, element=0):
        self.start = start
        self.end = end
        self.element = element