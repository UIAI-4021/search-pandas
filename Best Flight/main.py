"""
 _   _  _  _  ___ __   __ ___  ___  ___  ___  _____ __   __   ___   ___   ___  ___  ___    _    _  _    _    _  _
| | | || \| ||_ _|\ \ / /| __|| _ \/ __||_ _||_   _|\ \ / /  / _ \ | __| |_ _|/ __|| __|  /_\  | || |  /_\  | \| |
| |_| || .` | | |  \ V / | _| |   /\__ \ | |   | |   \ V /  | (_) || _|   | | \__ \| _|  / _ \ | __ | / _ \ | .` |
 \___/ |_|\_||___|  \_/  |___||_|_\|___/|___|  |_|    |_|    \___/ |_|   |___||___/|_|  /_/ \_\|_||_|/_/ \_\|_|\_|

Title: Best flight project
Author: - Melika Shirian
        - Kianoosh vadaei
Date: 2023-11-04
Description:
    This project is part of the "Fundamentals and Applications of Artificial Intelligence" course at the University of Isfahan.

    Our mission in this project is to tackle the complex challenge of optimizing flight routes across different countries. To do this, we've harnessed a relatively large dataset comprising real flights originating from various airports in different countries, each associated with different pricing and distances.
Ffi
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
import os.path

# region  Libraries
# ==========================
from Graph import Graph
from Heap import Entry
import time
import sys
# endregion


# region Forming the Graph
# ==========================
graph = Graph.getInstance() #getting the only instance of the Graph
graph.form_graph()
graph_time = time.time()    #temp
# endregion

# region Getting The input
# ==========================
try:
    if len(sys.argv) < 2:
        raise ValueError("Usage: python best-flight.py \"Source Airport - Destination Airport\"")
    input = sys.argv[1].strip('"')  # ---> The inputs should be given by calling the script best-flight and inputs
    #     Usage: python best-flight.py input1 - input2

    src = input.split(' - ')[0]
    dst = input.split(' - ')[1]

    source_vertex = graph.get_vertex(src)
    destination_vertex = graph.get_vertex(dst)

    if source_vertex is None or destination_vertex is None:
        raise ValueError('The Source Airport or Destination Airport does not exist')

except ValueError as e:
    print('\nError:' , e)
    # exit()

# endregion

dijkstra_start_time = time.time()    #To measure the execution time

dijkstra_entry = graph.dijkstra(graph.get_vertex('Imam Khomeini International Airport'),
                   graph.get_vertex('Raleigh Durham International Airport'))
# e = graph.dijkstra(source_vertex, destination_vertex)
dijkstra_end_time = time.time()


a_star_start_time = time.time()    #To measure the execution time

a_star_entry = graph.a_star(graph.get_vertex('Imam Khomeini International Airport'),
                            graph.get_vertex('Raleigh Durham International Airport'))
# a_star_entry = graph.dijkstra(source_vertex, destination_vertex)
a_star_end_time = time.time()


# region Print dijkstra

if not os.path.exists('../Best Flight Output'):
    os.mkdir('../Best Flight Output')
file = open('../Best Flight Output/Dijkstra-Algorithm.txt', 'w', encoding="utf-8")


dijkstra_execution_time = round(dijkstra_end_time - dijkstra_start_time,3)

total_price = 0
total_duration = 0
total_time = 0

print('\n#############') #result Seprator
file.write('#############\n')

print('Dijkstra Algorithm')
file.write('Dijkstra Algorithm\n')
if dijkstra_execution_time >= 60:
    print(f'Execution Time: {round(dijkstra_execution_time / 60, 3)}min{round(dijkstra_execution_time % 60, 3)}s')
    file.write(f'Execution Time: {round(dijkstra_execution_time / 60, 3)}min{round(dijkstra_execution_time % 60, 3)}s\n')
else:
    print(f'Execution Time: {round(dijkstra_execution_time, 3)}s')
    file.write(f'Execution Time: {round(dijkstra_execution_time, 3)}s\n')
print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
file.write('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n')

if isinstance(dijkstra_entry , Entry):
    for i in range(0 , len(dijkstra_entry.path) - 1):
        src = graph.get_vertex(dijkstra_entry.path[i].name)
        dst = graph.get_vertex(dijkstra_entry.path[i + 1].name)
        path = graph.get_edge(src , dst)

        print(f'Flight #{i+1}:')
        file.write(f'Flight #{i+1}:\n')
        print(f'From: {src.name} - {src.city}, {src.country}')
        file.write(f'From: {src.name} - {src.city}, {src.country}\n')
        print(f'To: {dst.name} - {dst.city}, {dst.country}')
        file.write(f'To: {dst.name} - {dst.city}, {dst.country}\n')
        print(f'Duration: {round(path.duration, 3)}km')
        file.write(f'Duration: {round(path.duration, 3)}km\n')
        time = path.time

        if path.time < 1:
            print(f'Time: {round(path.time * 60)}min')
            file.write(f'Time: {round(path.time * 60)}min\n')
        else:
            print(f'Time: {int(path.time)}h {round((path.time - int(path.time)) * 60)}min')
            file.write(f'Time: {int(path.time)}h {round((path.time - int(path.time)) * 60)}min\n')

        print(f'Price: {round(path.price, 3)}$')
        file.write(f'Price: {round(path.price, 3)}$\n')
        print('----------------------------')
        file.write('----------------------------\n')

        total_price += path.price
        total_duration = path.duration
        total_time = path.time

print(f'Total Price: {total_price}$')
file.write(f'Total Price: {total_price}$\n')
print(f'Total Duration: {round(total_duration,3)}km')
file.write(f'Total Duration: {round(total_duration,3)}km\n')
if total_time < 1:
    print(f'Total Time: {round(total_time * 60)}min')
    file.write(f'Total Time: {round(total_time * 60)}min\n')
else:
    print(f'Total Time: {int(total_time)}h {round((total_time - int(total_time)) * 60)}min')
    file.write(f'Total Time: {int(total_time)}h {round((total_time - int(total_time)) * 60)}min\n')

file.close()
# endregion

# ==========================

# region Print A*

if not os.path.exists('../Best Flight Output'):
    os.mkdir('../Best Flight Output')
file = open('../Best Flight Output/A-Star-Algorithm.txt', 'w', encoding="utf-8")


a_star_execution_time = round(a_star_end_time - a_star_start_time, 3)

total_price = 0
total_duration = 0
total_time = 0

print('\n#############') #result Seprator
file.write('#############\n')

print('A* Algorithm')
file.write('A* Algorithm\n')
if a_star_execution_time >= 60:
    print(f'Execution Time: {round(a_star_execution_time / 60, 3)}min{round(a_star_execution_time % 60, 3)}s')
    file.write(f'Execution Time: {round(a_star_execution_time / 60, 3)}min{round(a_star_execution_time % 60, 3)}s\n')
else:
    print(f'Execution Time: {round(a_star_execution_time, 3)}s')
    file.write(f'Execution Time: {round(a_star_execution_time, 3)}s\n')
print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
file.write('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-\n')

if isinstance(a_star_entry, Entry):
    for i in range(0 , len(a_star_entry.path) - 1):
        src = graph.get_vertex(a_star_entry.path[i].name)
        dst = graph.get_vertex(a_star_entry.path[i + 1].name)
        path = graph.get_edge(src , dst)

        print(f'Flight #{i+1}:')
        file.write(f'Flight #{i+1}:\n')
        print(f'From: {src.name} - {src.city}, {src.country}')
        file.write(f'From: {src.name} - {src.city}, {src.country}\n')
        print(f'To: {dst.name} - {dst.city}, {dst.country}')
        file.write(f'To: {dst.name} - {dst.city}, {dst.country}\n')
        print(f'Duration: {round(path.duration, 3)}km')
        file.write(f'Duration: {round(path.duration, 3)}km\n')
        time = path.time

        if path.time < 1:
            print(f'Time: {round(path.time * 60)}min')
            file.write(f'Time: {round(path.time * 60)}min\n')
        else:
            print(f'Time: {int(path.time)}h {round((path.time - int(path.time)) * 60)}min')
            file.write(f'Time: {int(path.time)}h {round((path.time - int(path.time)) * 60)}min\n')

        print(f'Price: {round(path.price, 3)}$')
        file.write(f'Price: {round(path.price, 3)}$\n')
        print('----------------------------')
        file.write('----------------------------\n')

        total_price += path.price
        total_duration = path.duration
        total_time = path.time

print(f'Total Price: {total_price}$')
file.write(f'Total Price: {total_price}$\n')
print(f'Total Duration: {round(total_duration,3)}km')
file.write(f'Total Duration: {round(total_duration,3)}km\n')
if total_time < 1:
    print(f'Total Time: {round(total_time * 60)}min')
    file.write(f'Total Time: {round(total_time * 60)}min\n')
else:
    print(f'Total Time: {int(total_time)}h {round((total_time - int(total_time)) * 60)}min')
    file.write(f'Total Time: {int(total_time)}h {round((total_time - int(total_time)) * 60)}min\n')

file.close()
# endregion

