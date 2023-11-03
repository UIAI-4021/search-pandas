class VertexClass:

    def __init__(self, name):
        self.name = name
        self.startings = dict()
        self.endings = dict()

    def add_ending(self, vertex_to_be_connected , edge):
        self.endings[vertex_to_be_connected] = edge

    def add_starting(self, vertex_to_be_connected, edge):
        self.startings[vertex_to_be_connected] = edge
