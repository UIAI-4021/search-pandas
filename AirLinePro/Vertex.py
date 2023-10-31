class VertexClass:

    connected_vertices : dict
    def __init__(self,name):
        self.name = name

    def add_link(self, vertex_to_be_connected , edge):
        self.connected_vertices[vertex_to_be_connected] = edge


