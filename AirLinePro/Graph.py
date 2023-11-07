from tqdm import tqdm

from Flight import Flight
from Heap import Heap, Entry
from Vertex import VertexClass
from Edge import EdgeClass
class Graph :

    # singleTon graph
    _instance = None
    edges : set
    vertices : set
    # first we append all our vertices in the graph
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

    def add_edge(self ,starting : VertexClass, ending : VertexClass, duration , time , price , cost):
        if self.get_edge(starting , ending) is None:
            edge = EdgeClass(starting, ending,duration , time , price, cost)
            starting.add_ending(ending , edge)
            ending.add_starting(starting , edge)
            self.edges.add(edge)


    def form_graph(self):
        flights = Flight.get_flights()
        for flight in tqdm(flights, desc='Forming the graph'.upper(), unit='vertex'):
            if self.get_vertex(flight.SourceAirport) is None:
                self.add_vertex(VertexClass(flight.SourceAirport, flight.SourceAirport_City, flight.SourceAirport_Country))
            if self.get_vertex(flight.DestinationAirport ) is None:
                self.add_vertex(VertexClass(flight.DestinationAirport, flight.DestinationAirport_City , flight.DestinationAirport_Country))

            starting = self.get_vertex(str(flight.SourceAirport))
            ending = self.get_vertex(str(flight.DestinationAirport))
            last_edge = self.get_edge(starting, ending)

            if last_edge is None or last_edge.cost > flight.Cost:
                self.add_edge(starting, ending, duration=flight.Distance, time=flight.FlyTime, price=flight.Price, cost=flight.Cost)

    def dijkstra(self, origin: VertexClass, destination: VertexClass):

        total_iterations = len(self.vertices)
        progress_bar = tqdm(total=total_iterations, desc='finding the best path with the Dijkstra\'s algorithm'.upper(),
                            unit="Vertex")

        visited_graph = set()

        # making our heap and adding the origin as the starting point of the dijkstra
        root_value = []
        heap = Heap()
        heap.inster(0, root_value, origin)

        while len(visited_graph) != len(self.vertices):
            next_path = heap.remove_min()

            if next_path.flight_info.name == destination.name:
                next_path.path.append(next_path.flight_info)
                return next_path

            last_path = None

            if isinstance(next_path, Entry):  # we want to expand the last destination we had
                last_path = next_path.flight_info
                visited_graph.add(next_path.flight_info.name)

            vertex = None
            for item in self.vertices:
                if item.name == last_path.name:
                    vertex = item
                    break

            # finding the next destinations that we can go using this last path that we went
            updated_path = list()
            for i in next_path.path:
                updated_path.append(i)
            updated_path.append(vertex)

            # next_path.path.append(next_path.flight_info)
            # updated_path = next_path.path

            for item in vertex.endings:
                flag = False
                if isinstance(item, VertexClass):
                    # already has been checked
                    for name in visited_graph:
                        if item.name == name:
                            flag = True
                            break
                    if flag:
                        continue

                e = vertex.endings[item]
                heap.inster(e.cost + next_path.key, updated_path, item)
            progress_bar.update(1)

        return None

