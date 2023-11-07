class VertexClass:

    def __init__(self, name, city, country, x_axis , y_axis, z_axis):
        self.name = name
        self.country = country
        self.city = city
        self.startings = dict()
        self.endings = dict()
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.z_axis = z_axis

    def add_ending(self, vertex_to_be_connected , edge):
        self.endings[vertex_to_be_connected] = edge

    def add_starting(self, vertex_to_be_connected, edge):
        self.startings[vertex_to_be_connected] = edge
