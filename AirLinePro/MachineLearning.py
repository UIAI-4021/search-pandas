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
                                                        Y_price, test_size=0.2, shuffle=True)

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
    def finding_w(problem, max_epochs, batch_size, learning_rate):

        w = 0
        converged_w = 0
        pre_w = None
        for t in range(0,max_epochs):
            if converged_w >= 100:
                break
            elif converged_w > 0 and pre_w == t:
                converged_w += 1
            else:
                converged_w = 1

            for batch in MyML.get_batches(problem.data, batch_size):
                w = MyML.get_derivation(w, batch, learning_rate)


    @staticmethod
    def get_batches(data, batch_size):
        # Helper function to generate mini-batches from the data
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]
    @staticmethod
    def get_derivation(w, b, alpha):
        w, b = symbols('w b')
        expr = b/w
        expr_diff = Derivative(expr, w, b)

        return w - (alpha * expr_diff)


    def gradient_descent(problem, max_epochs, batch_size, learning_rate):
        # Initialize parameters
        x = initialize_parameters(problem.model_type)

        # Set initial epoch
        t = 0

        # Set convergence criteria (you need to define this based on your problem)
        converged = False

        while t < max_epochs and not converged:
            # Iterate over batches
            for batch in get_batches(problem.data, batch_size):
                # Compute gradients
                gradients = compute_gradients(problem, x, batch)

                # Update parameters using gradients and learning rate
                x = update_parameters(x, gradients, learning_rate)

                # Increment epoch
                t += 1

            # Check for convergence based on your criteria
            # You need to implement the convergence check based on your problem
            converged = check_convergence(x, problem)

        return x


