# caller.py

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
# Call main.py with the inputs
try:
    if sys.platform == 'win32':
        # noinspection PyUnboundLocalVariable
        os.system(f'python ../AirLinePro/main.py \"{input}\"')
    else:
        # noinspection PyUnboundLocalVariable
        os.system(f'python3 ../AirLinePro/main.py \"{input}\"')

except Exception as e:
    print(f"Error: {e}")
