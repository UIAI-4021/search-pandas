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

#region inports
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from MachineLearning import MyML
from globals import _flight_price_dataset
import pandas as pd
#endregion

# pre-process
# ==============================
df = pd.read_csv(_flight_price_dataset)
MyML.scaler(df)
df = MyML.label_encode(df)
X_train, X_test, y_train, y_test = MyML.split(df)

# some gradient descent settings
# ==============================
m, n = X_train.shape
initial_w = np.zeros((n,))
initial_b = 0.
iterations = m
_ALFA = 0.006

start = time.time()

w_final, b_final, J_hist = MyML.gradient_descent(X_train, y_train, initial_w, initial_b, _ALFA, iterations)

end = time.time()
training_time = end - start

# predict
# ==============================
m, _ = X_test.shape
pre = []
for i in range(m):
    pre.append(np.dot(X_test[i], w_final) + b_final)

mae, mse, rmse, r2 = MyML.calculate_error(y_test, pre)

#region output
if not os.path.exists('../Multiple Linear Regression Output'):
    os.mkdir('../Multiple Linear Regression Output')
file = open('../Multiple Linear Regression Output/Pandas-UIAI4021-PR1-Q2.txt', 'w', encoding="utf-8")

print('PRICE = ', end='')
file.write('PRICE = ')
for i in range(len(w_final)):
    print(f'{w_final[i]} * {df.columns[i]}' , end='')
    file.write(f'{w_final[i]} * {df.columns[i]}')
    if i != (len(w_final) - 1):
        print(' + ', end='')
        file.write(' + ')
print(f'\nTraining Time: {training_time}s\n')
file.write(f'\nTraining Time: {training_time}s\n\n')

print(f'Logs:\n'
      f'MSE: {mse}\n'
      f'RMSE: {rmse}\n'
      f'MAE: {mae}\n'
      f'R2: {r2}')
file.write(f'Logs:\n'
      f'MSE: {mse}\n'
      f'RMSE: {rmse}\n'
      f'MAE: {mae}\n'
      f'R2: {r2}')
#endregion

#region plot
plt.plot(J_hist, label='Cost vs. Iteration', color='magenta', linestyle='-' )
plt.title("Cost vs. Iteration")
plt.xlabel('Iteration Step')
plt.ylabel('Cost(MSE)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig('../Multiple Linear Regression Output/Cost-plot.png')
plt.show()
#endregion

