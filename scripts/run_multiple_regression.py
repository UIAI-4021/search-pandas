"""
 _   _  _  _  ___ __   __ ___  ___  ___  ___  _____ __   __   ___   ___   ___  ___  ___    _    _  _    _    _  _
| | | || \| ||_ _|\ \ / /| __|| _ \/ __||_ _||_   _|\ \ / /  / _ \ | __| |_ _|/ __|| __|  /_\  | || |  /_\  | \| |
| |_| || .` | | |  \ V / | _| |   /\__ \ | |   | |   \ V /  | (_) || _|   | | \__ \| _|  / _ \ | __ | / _ \ | .` |
 \___/ |_|\_||___|  \_/  |___||_|_\|___/|___|  |_|    |_|    \___/ |_|   |___||___/|_|  /_/ \_\|_||_|/_/ \_\|_|\_|

Title: Multiple Linear Regression project
Author: - Melika Shirian
        - Kianoosh vadaei
Date: 2023-11-04
Description:
This project implements a multiple linear regression model for predicting flight prices. The team developed custom solutions and leveraged scikit-learn for scaling and labeling, demonstrating a blend of manual implementation and established tools.

The dataset includes six features, expanded to 15 after one-hot labeling. Notable output includes the "Cost per Iteration" plot in the regression output folder, providing insights into the training process.

Usage:
You can run this script by executing it from the command line, providing necessary arguments and options. Example usage:

python script/run_multiple_regression.py

Requirements:
    - Python 3.x
    - "tqdm" library for progress bar support
    - pandas
    - numpy
    - scikit-learn
    - matplotlib

Contributors:
    - Kianoosh Vadaei
    - Melika Shirian

Notes:
    - This project is undertaken as part of the "Fundamentals and Applications of Artificial Intelligence" course at the University of Isfahan, instructed by Dr. Hossein Karshenas.
    - Teaching Assistants for the course are Kian Majlesi and Audrina Ebrahimi.

"""


import os
import sys
try:
    if sys.platform == 'win32':
        os.system(f'python \"../Multiple Linear Regression/main.py\"')
    else:
        os.system(f'python3 \"../Multiple Linear Regression/main.py\"')
except Exception as e:
    print(f"Error: {e}")
