import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from MachineLearning import MyML
from ./../Best Flight/globals import _flight_price_dataset
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
print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
m, _ = X_test.shape
pre = []
for i in range(m):
    print(f"prediction: {np.dot(X_test[i], w_final) + b_final:0.2f}, target value: {y_test[i]}")
    pre.append(np.dot(X_test[i], w_final) + b_final)

print(end - start)

MyML.checking_error(y_test, pre)



plt.plot(J_hist, label='Cost vs. Iteration', color='magenta', linestyle='-' )

# Title and labels
plt.title("Cost vs. iteration")
plt.xlabel('Iteration Step')
plt.ylabel('Cost')

# Grid
plt.grid(True, linestyle='--', alpha=0.7)

# Legend
plt.legend()

# Display the plot
plt.show()


