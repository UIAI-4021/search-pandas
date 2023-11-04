from Flight import Flight
from Vertex import VertexClass
from Graph import Graph
from Heap import Entry
import time
from tqdm import tqdm

start_time = time.time()

graph = Graph.getInstance()
graph.form_flights()

graph_time = time.time()

e = graph.dijkstra(graph.get_vertex('Imam Khomeini International Airport'),
                   graph.get_vertex('Raleigh Durham International Airport'))

f = open('./tmp.txt', 'w', encoding="utf-8")

i = 1
if isinstance(e, Entry):
    for item in e.path:
        print(f'{i} : {item.name}')
        f.write(f'{i} : {item.name}\n')
        i += 1

end_time = time.time()
f.write(f'graph time: {graph_time - start_time} \n execution time: {end_time - start_time}\n')
