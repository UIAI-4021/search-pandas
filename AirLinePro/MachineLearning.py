import copy
import math

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


class MyML:

    @staticmethod
    def label_encode(flight_price_df):
        time_mapping = {
            'Early_Morning': 1,
            'Morning': 2,
            'Afternoon': 3,
            'Evening': 4,
            'Night': 5,
            'Late_Night': 6
        }

        stops_mapping = {
            'zero': 1,
            'one': 2,
            'two_or_more': 3
        }
        class_mapping = {
            'Economy': 1,
            'Business': 2
        }

        flight_price_df['departureTimeMapping'] = flight_price_df['departure_time'].map(time_mapping)
        flight_price_df['arrivalTimeMapping'] = flight_price_df['arrival_time'].map(time_mapping)
        flight_price_df['stopsMapping'] = flight_price_df['stops'].map(stops_mapping)
        flight_price_df['classMapping'] = flight_price_df['class'].map(class_mapping)

    @staticmethod
    def data_set_split(flight_price_df):
        X_departure_time = np.array(flight_price_df['departureTimeMapping'])
        X_arrival_time = np.array(flight_price_df['arrivalTimeMapping'])
        X_stops = np.array(flight_price_df['stopsMapping'])
        X_flight_class = np.array(flight_price_df['classMapping'])
        X_duration = np.array(flight_price_df['duration'])
        X_days_left = np.array(flight_price_df['days_left'])
        y_price = np.array(flight_price_df['price'])

        X_departure_time_train, X_departure_time_test, \
        X_arrival_time_train, X_arrival_time_test,\
        X_stops_train, X_stops_test,\
        X_flight_class_train, X_flight_class_test,\
        X_duration_train, X_duration_test,\
        X_days_left_train, X_days_left_test,\
        y_price_train, y_price_test = train_test_split(X_departure_time, X_arrival_time,
                                                        X_stops, X_flight_class,
                                                        X_duration, X_days_left,
                                                        y_price, test_size=0.2, shuffle=True)

        X_train = np.array([X_departure_time_train,
        X_arrival_time_train,
        X_stops_train,
        X_flight_class_train,
        X_duration_train,
        X_days_left_train])

        y_train = np.array(y_price_train)

        X_test = np.array([X_departure_time_test, X_arrival_time_test, X_stops_test, X_flight_class_test,
                  X_duration_test, X_days_left_test])

        y_test = np.array(y_price_test)

        return X_train, X_test, y_train, y_test


    @staticmethod
    def compute_gradient(X, y, w, b):
        """
        Computes the gradient for linear regression
        Args:
          X (ndarray (m,n)): Data, m examples with n features
          y (ndarray (m,)) : target values
          w (ndarray (n,)) : model parameters
          b (scalar)       : model parameter

        Returns:
          dj_dw (ndarray (n,)): The gradient of the cost w.r.t. the parameters w.
          dj_db (scalar):       The gradient of the cost w.r.t. the parameter b.
        """
        m, n = X.shape  # (number of examples, number of features)
        dj_dw = np.zeros((n,))
        dj_db = 0.

        for i in range(m):
            err = (np.dot(X[i], w) + b) - y[i]
            for j in range(n):
                dj_dw[j] = dj_dw[j] + err * X[i, j]
            dj_db = dj_db + err
        dj_dw = dj_dw / m
        dj_db = dj_db / m

        return dj_db, dj_dw
    @staticmethod
    def gradient_descent(X, y, w_in, b_in, alpha, num_iters):
        """
        Performs batch gradient descent to learn w and b. Updates w and b by taking
        num_iters gradient steps with learning rate alpha

        Args:
          X (ndarray (m,n))   : Data, m examples with n features
          y (ndarray (m,))    : target values
          w_in (ndarray (n,)) : initial model parameters
          b_in (scalar)       : initial model parameter
          alpha (float)       : Learning rate
          num_iters (int)     : number of iterations to run gradient descent

        Returns:
          w (ndarray (n,)) : Updated values of parameters
          b (scalar)       : Updated value of parameter
          """

        # An array to store cost J and w's at each iteration primarily for graphing later
        w_history = []
        w = copy.deepcopy(w_in)  # avoid modifying global w within function
        b = b_in

        converged = False
        for i in range(num_iters) and (not converged):

            # Calculate the gradient and update the parameters
            dj_db, dj_dw = MyML.compute_gradient(X, y, w, b)

            # Update Parameters using w, b, alpha and gradient
            w = w - alpha * dj_dw
            b = b - alpha * dj_db

            w_history.append(w)

            converged_tmp = w
            a = 0
            for j in range(len(w_history), len(w_history)-100, -1):
                if abs(converged_tmp - w_history[j]) < 0.00001:
                    continue
                else:
                    a = 1
            if a == 0:
                converged = True


        return w, b
