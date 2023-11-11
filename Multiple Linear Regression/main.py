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
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from MachineLearning import MyML
from globals import _flight_price_dataset
import pandas as pd

df = pd.read_csv(_flight_price_dataset)
MyML.scaler(df)
df = MyML.label_encode(df)
X_train, X_test, y_train, y_test = MyML.split(df)


m,n = X_train.shape
initial_w = np.zeros((n,))
initial_b = 0.
# some gradient descent settings
iterations = m
_ALFA = 0.006
# run gradient descent
start = time.time()

w_final, b_final, J_hist = MyML.gradient_descent(X_train, y_train, initial_w, initial_b, _ALFA, iterations)

end = time.time()
# print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
m, _ = X_test.shape
pre = []
for i in range(m):
    # print(f"prediction: {np.dot(X_test[i], w_final) + b_final:0.2f}, target value: {y_test[i]}")
    pre.append(np.dot(X_test[i], w_final) + b_final)

training_time = end - start

mae, mse, rsme, r2 = MyML.calculate_error(y_test, pre)

#region output
if not os.path.exists('../Multiple Linear Regression Output'):
    os.mkdir('../Multiple Linear Regression Output')
file = open('../Multiple Linear Regression Output/Output.txt', 'w', encoding="utf-8")


#endregion

plt.plot(J_hist, label='Cost vs. Iteration', color='magenta', linestyle='-' )
plt.title("Cost vs. iteration")
plt.xlabel('Iteration Step')
plt.ylabel('Cost')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()


