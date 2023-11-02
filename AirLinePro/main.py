import pandas as pd
from Flight import Flight
from Vertex import VertexClass
from Graph import Graph
from Edge import EdgeClass
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

