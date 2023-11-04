"""
 _   _  _  _  ___ __   __ ___  ___  ___  ___  _____ __   __     ___   ___     ___  ___  ___    _    _  _    _    _  _
| | | || \| ||_ _|\ \ / /| __|| _ \/ __||_ _||_   _|\ \ / /    / _ \ | __|   |_ _|/ __|| __|  /_\  | || |  /_\  | \| |
| |_| || .` | | |  \ V / | _| |   /\__ \ | |   | |   \ V /    | (_) || _|     | | \__ \| _|  / _ \ | __ | / _ \ | .` |
 \___/ |_|\_||___|  \_/  |___||_|_\|___/|___|  |_|    |_|      \___/ |_|     |___||___/|_|  /_/ \_\|_||_|/_/ \_\|_|\_|

Title: Best flight project
Author: - Melika Shirian
        - Kianoosh vadaei
Date: 2023-11-04
Description:
    This project is part of the "Fundamentals and Applications of Artificial Intelligence" course at the University of Isfahan.

    Our mission in this project is to tackle the complex challenge of optimizing flight routes across different countries. To do this, we've harnessed a relatively large dataset comprising real flights originating from various airports in different countries, each associated with different pricing and distances.

    The primary objective is to identify the most efficient and cost-effective routes for travelers, ensuring that the journeys between countries are both optimal and economical. To achieve this goal, we've explored two key algorithms, Dijkstra and A*, as tools to navigate our extensive flight network.

    In addition to these algorithms, we've leveraged essential data structures, including the use of a min-heap, to manage and streamline our graph-based approach.

    Our project represents a real-world application of artificial intelligence, demonstrating how advanced algorithms and data structures can be employed to solve complex routing problems in the aviation industry.

Usage:
    You can run this script by executing it from the command line, providing necessary arguments and options. Example usage:

    $ python my_project.py [arguments] [options]

Requirements:
    - Python 3.x
    - "art" library for ASCII art generation
    - "tqbm" library for progress bar support

Contributors:
    - Kianoosh Vadaei
    - Melika Shirian

Notes:
    - This project is undertaken as part of the "Fundamentals and Applications of Artificial Intelligence" course at the University of Isfahan, instructed by Dr. Hossein Karshenas.
    - Teaching Assistants for the course are Kian Majlesi and Audrina Ebrahimi.

"""

# region  Libraries
# ==========================
from Flight import Flight
from Vertex import VertexClass
from Graph import Graph
from Heap import Entry
import time
# endregion

start_time = time.time()    #To measure the execution time

# region Forming the Graph
# ==========================
graph = Graph.getInstance() #getting the only instance of the Graph
graph.form_flights()
graph_time = time.time()    #temp
# endregion

# region Getting The input

# ==========================

# endregion

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
