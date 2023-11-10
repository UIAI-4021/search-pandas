import time

import matplotlib
matplotlib.use('TkAgg')  # You can replace 'TkAgg' with the backend of your choice, e.g., 'Qt5Agg', 'Agg', etc.
import matplotlib.pyplot as plt
import numpy as np

from MachineLearning import MyML
from Flight import FlightPrice

df = FlightPrice.get_flights_price()
MyML.label_encode(df)
MyML.scaler(df)
X_train, X_test, y_train, y_test = MyML.split(df)


m,n = X_train.shape
initial_w = np.zeros((n,))
initial_b = 0.
# some gradient descent settings
iterations = m
alpha = 0.0008
# run gradient descent
start = time.time()
w_final, b_final, J_hist = MyML.gradient_descent(X_train, y_train, initial_w, initial_b, alpha, iterations)
end = time.time()
print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
m, _ = X_train.shape
pre = []
for i in range(m):
    print(f"prediction: {np.dot(X_train[i], w_final) + b_final:0.2f}, target value: {y_train[i]}")
    pre.append(np.dot(X_train[i], w_final) + b_final)

print(end - start)

MyML.checking_error(y_train, pre)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
fig.tight_layout()

ax1.plot(J_hist)
ax1.set_title("Cost vs. iteration")
ax1.set_ylabel('Cost')
ax1.set_xlabel('iteration step')

plt.show()




# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
# fig.tight_layout()
#
# ax1.plot(J_hist)
# ax1.set_title("Cost vs. iteration")
# ax1.set_ylabel('Cost')
# ax1.set_xlabel('iteration step')
#
# plt.show()
#