
from Vertex import VertexClass

class EdgeClass:
    def __init__(self , start : VertexClass, end : VertexClass, cost=0):
        self.start = start
        self.end = end
        self.cost = cost
