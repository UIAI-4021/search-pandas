
from Vertex import VertexClass

class EdgeClass:
    def __init__(self , start : VertexClass, end : VertexClass, duration,time , price, cost):
        self.start = start
        self.end = end
        self.cost = cost
        self.duration = duration
        self.time = time
        self.price = price
