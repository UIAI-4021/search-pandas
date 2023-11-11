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

    $ python run_best_flight.py "flight1 - flight2"

Requirements:
    - Python 3.x
    - "tqbm" library for progress bar support

Contributors:
    - Kianoosh Vadaei
    - Melika Shirian

Notes:
    - This project is undertaken as part of the "Fundamentals and Applications of Artificial Intelligence" course at the University of Isfahan, instructed by Dr. Hossein Karshenas.
    - Teaching Assistants for the course are Kian Majlesi and Audrina Ebrahimi.

"""
import os
import sys

# Define your inputs
try:
    if len(sys.argv) < 2:
        raise ValueError("Usage: python best-flight.py \"Source Airport - Destination Airport\"")
    input = sys.argv[1].strip('"')     # ---> The inputs should be given by calling the script best-flight and inputs
                                        # Usage: python best-flight.py input1 - input2
except ValueError as e:
    print('\nError:', e)
    exit()
try:
    if sys.platform == 'win32':
        os.system(f'python "../Best Flight/main.py" "{input}"')
    else:
        os.system(f'python3 \"../Best Flight/main.py\" \"{input}\"')

except Exception as e:
    print(f"Error: {e}")
