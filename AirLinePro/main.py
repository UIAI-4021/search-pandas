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
               ,record['Distance'] ,record['FlyTime'] ,record['Price'] ,0)

        flights.append(f)
    return flights



flights = set_data(df)
max = 0
for i in flights:
    if i.FlyTime > max:
        max = i.FlyTime
print(max)
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
#     if last_edge is None or last_edge.cost > record['Price']:
#         graph.add_edge(starting , ending , cost=record['Price'])
# print()
#
#
#
#
def dijkstra (graph : Graph , destination: VertexClass , origin: VertexClass):

    visited_graph = set()

    # making our heap and adding the origin as the starting point of the dijkstra
    root_value = [origin]
    heap = Heap()
    heap.inster(0, root_value)

    while len(visited_graph) != len(graph.vertices):
        next_path = heap.remove_min()


        last_path = None

        if isinstance(next_path, Entry): # we want to expand the last destination we had
            last_path = next_path.flight_info
            visited_graph.add(next_path.flight_info.DestinationAirport)

        vertex = None
        for item in graph.vertices:
            if item.name == last_path.DestinationAirport:
                vertex = item

        # finding the next destinations that we can go using this last path that we went
        next_path.value.append(next_path)

        for item in vertex.connected_vertices:


            if isinstance(item, VertexClass):
                for name in visited_graph:
                    if name == item.name:
                        continue
            heap.inster(item.cost + next_path.key, next_path.path)



