import pandas as pd
from Flight import Flight
from Vertex import VertexClass
from Graph import Graph
from Edge import EdgeClass
from Heap import Heap
from Heap import Entry

df = pd.read_csv('../assets/files/Flight_Data_Reduced.csv')

def set_data(records):
    flights = list()
    for index, record in df.iterrows():
        primary_pow = 10**3
        # cost = 6 * record['Price'] + 3 * record['FlyTime'] + record['Distance']   #kianoosh`s way
        cost = record['Distance'] * primary_pow + record['FlyTime'] * primary_pow * (10**2) +\
               record['Price'] * primary_pow * (10**2) * (10**3)    #melika`s way

        f = Flight(record['Airline'] , record['SourceAirport'] ,record['DestinationAirport']
               ,record['SourceAirport_City'] ,record['SourceAirport_Country']
               ,record['SourceAirport_Latitude'] ,record['SourceAirport_Longitude']
               , record['SourceAirport_Altitude'] ,record['DestinationAirport_City']
               ,record['DestinationAirport_Country'] ,record['DestinationAirport_Latitude']
               ,record['DestinationAirport_Longitude'] ,record['DestinationAirport_Altitude']
               ,record['Distance'] ,record['FlyTime'] ,record['Price'] ,cost)

        flights.append(f)
    return flights



flights = set_data(df)

#
#
# graph = Graph.getInstance()
# for flight in flights:
#     if graph.get_vertex(flight.SourceAirport) is None:
#         graph.add_vertex(VertexClass(flight.SourceAirport))
#     if graph.get_vertex(flight.DestinationAirport) is None:
#         graph.add_vertex(VertexClass(flight.DestinationAirport))
#
# for i , record in df.iterrows():
#     starting = graph.get_vertex(str(record['SourceAirport']))
#     ending = graph.get_vertex(str(record['DestinationAirport']))
#     last_edge = graph.get_edge(starting , ending)
#     if last_edge is None or last_edge.cost > record['cost']:
#         graph.add_edge(starting , ending , cost=record['cost'])
# print()
#
#
#
#


graph = Graph.getInstance()
V1 = VertexClass('A')
V2 = VertexClass('B')
V3 = VertexClass('C')
V4 = VertexClass('D')
V5 = VertexClass('E')
V6 = VertexClass('F')
graph.add_vertex(V1)
graph.add_vertex(V2)
graph.add_vertex(V3)
graph.add_vertex(V4)
graph.add_vertex(V5)
graph.add_vertex(V6)
graph.add_edge(V1 , V2 , 10)
graph.add_edge(V1 , V3 , 15)
graph.add_edge(V2 , V4 , 12)
graph.add_edge(V2 , V6 , 15)
graph.add_edge(V4 , V6 , 1)
graph.add_edge(V6 , V5 , 5)
graph.add_edge(V4 , V5 , 2)
graph.add_edge(V3 , V5 , 10)


def dijkstra (graph : Graph , origin: VertexClass, destination: VertexClass):

    visited_graph = set()

    # making our heap and adding the origin as the starting point of the dijkstra
    root_value = []
    heap = Heap()
    heap.inster(0, root_value, origin)

    while len(visited_graph) != len(graph.vertices):
        next_path = heap.remove_min()


        last_path = None

        if isinstance(next_path, Entry): # we want to expand the last destination we had
            last_path = next_path.flight_info
            visited_graph.add(next_path.flight_info.name)

        vertex = None
        for item in graph.vertices:
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

        if next_path.flight_info.name == destination:
            return next_path

        for item in vertex.endings:
            if isinstance(item, VertexClass):
                # already has been checked
                for name in visited_graph:
                    if name == item.name:
                        continue
            e = vertex.endings[item]
            heap.inster(e.cost + next_path.key, updated_path, item)

    return None



e = dijkstra(graph , V1 , V5)
print()