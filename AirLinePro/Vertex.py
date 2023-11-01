class VertexClass:

    def __init__(self,name):
        self.name = name
        self.connected_vertices = dict()

    def add_link(self, vertex_to_be_connected , edge):
        self.connected_vertices[vertex_to_be_connected] = edge


