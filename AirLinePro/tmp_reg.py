import time

import numpy as np
from sympy.physics.control.control_plots import plt

from MachineLearning import MyML
from Flight import FlightPrice

df = FlightPrice.get_flights_price()
X_train, X_test, y_train, y_test = MyML.data_set_split(df)


m,n = X_train.shape
initial_w = np.zeros((n,))
initial_b = 0.
m=20
# some gradient descent settings
iterations = m
alpha = 0.0000204
# run gradient descent
start = time.time()
w_final, b_final = MyML.gradient_descent(X_train[0:20], y_train[0:20], initial_w, initial_b, alpha, iterations)
end = time.time()
print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
m, _ = X_train.shape
for i in range(20):
    print(f"prediction: {np.dot(X_train[i], w_final) + b_final:0.2f}, target value: {y_train[i]}")

print(end - start)

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True, figsize=(12, 4))
ax1.plot(J_hist)
ax2.plot(100 + np.arange(len(J_hist[100:])), J_hist[100:])
ax1.set_title("Cost vs. iteration");  ax2.set_title("Cost vs. iteration (tail)")
ax1.set_ylabel('Cost')             ;  ax2.set_ylabel('Cost')
ax1.set_xlabel('iteration step')   ;  ax2.set_xlabel('iteration step')
plt.show()


