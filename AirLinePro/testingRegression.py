import numpy as np
import pandas as pd
from MachineLearning import MyML
from Flight import FlightPrice
from globals import _flight_price_dataset
def test():

    df, f = FlightPrice.get_flights_price()
    X_train, X_test, y_train, y_test = MyML.data_set_split(df)



    m,n = X_train.shape
    initial_w = np.zeros((n,))
    initial_b = 0.
    # some gradient descent settings
    iterations = m
    alpha = 0.00001
    # run gradient descent
    w_final, b_final = MyML.gradient_descent(X_train, y_train, initial_w, initial_b, alpha, iterations)
    print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
    m, _ = X_train.shape
    for i in range(m):
        print(f"prediction: {np.dot(X_train[i], w_final) + b_final:0.2f}, target value: {y_train[i]}")


test()
