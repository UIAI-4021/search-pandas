import copy
import math

from sklearn.preprocessing import StandardScaler
import sklearn
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from tqdm import tqdm


class MyML:

    @staticmethod
    def label_encode(flight_price_df):

        labeL_encoder = LabelEncoder()

        flight_price_df['departure_time'] = labeL_encoder.fit_transform(flight_price_df['departure_time'].values)
        flight_price_df['arrival_time'] = labeL_encoder.fit_transform(flight_price_df['arrival_time'].values)
        flight_price_df['stops'] = labeL_encoder.fit_transform(flight_price_df['stops'].values)
        flight_price_df['class'] = labeL_encoder.fit_transform(flight_price_df['class'].values)


    @staticmethod
    def scaler(flight_price_df):
        flight_price_df = pd.DataFrame(flight_price_df)
        scaler = StandardScaler()
        flight_price_df['days_left'] = scaler.fit_transform(flight_price_df['days_left'].values.reshape(-1,1))
        flight_price_df['duration'] = scaler.fit_transform(flight_price_df['duration'].values.reshape(-1,1))

    @staticmethod
    def split(flight_price_df):
        flight_price_df = pd.DataFrame(flight_price_df)

        x_train, x_test, y_train, y_test = train_test_split(
            flight_price_df.iloc[:, :-1].values,
            flight_price_df.iloc[:, -1].values.ravel(),
            shuffle=True,
            test_size=0.2
        )
        return x_train, x_test, y_train, y_test

    #
    @staticmethod
    def compute_cost(X, y, w, b):
        m = X.shape[0]
        err = (X @ w + b - y) ** 2
        cost = np.sum(err) / (2 * m)
        return cost


    @staticmethod
    def compute_gradient(X, y, w, b):
        m = X.shape[0]
        err = X @ w + b - y
        dj_dw = (X.T @ err) / m
        dj_db = np.sum(err) / m

        return dj_db, dj_dw


    @staticmethod
    def gradient_descent(X, y, w_in, b_in, alpha, num_iters):
        w_history = []
        J_history = []
        w = w_in.copy()
        b = b_in



        converged = False
        for i in tqdm(range(num_iters)):
            if converged:
                break

            dj_db, dj_dw = MyML.compute_gradient(X, y, w, b)

            w -= alpha * dj_dw
            b -= alpha * dj_db

            if i < 100000:
                J_history.append(MyML.compute_cost(X, y, w, b))

            w_history.append(w)

            if len(w_history) >= 10000:
                for j in range(len(w_history)-1, len(w_history)-100, -1):
                    if np.allclose(w_history[-1], w_history[j], atol=1e-5):
                        continue
                    else:
                        break
                else:
                    converged = True


        return w, b, J_history

    @staticmethod
    def checking_error(y_true, y_pred):
        # MAE
        mae = mean_absolute_error(y_true, y_pred)
        # MSE
        mse = mean_squared_error(y_true, y_pred)
        # RMSE
        rsme = math.sqrt(mse)
        # R2
        r2 = r2_score(y_true, y_pred)

        print(f'MAE: {mae}, MSE: {mse}, RMSE: {rsme}, R2: {r2}')

    # @staticmethod
    # def compute_gradient(X, y, w, b):
    #     """
    #     Computes the gradient for linear regression
    #     Args:
    #       X (ndarray (m,n)): Data, m examples with n features
    #       y (ndarray (m,)) : target values
    #       w (ndarray (n,)) : model parameters
    #       b (scalar)       : model parameter
    #
    #     Returns:
    #       dj_dw (ndarray (n,)): The gradient of the cost w.r.t. the parameters w.
    #       dj_db (scalar):       The gradient of the cost w.r.t. the parameter b.
    #     """
    #     m, n = X.shape  # (number of examples, number of features)
    #     dj_dw = np.zeros((n,))
    #     dj_db = 0.
    #
    #     for i in range(m):
    #         err = (np.dot(X[i], w) + b) - y[i]
    #         for j in range(n):
    #             dj_dw[j] = dj_dw[j] + err * X[i, j]
    #         dj_db = dj_db + err
    #     dj_dw = dj_dw / m
    #     dj_db = dj_db / m
    #
    #     return dj_db, dj_dw
    # @staticmethod
    # def gradient_descent(X, y, w_in, b_in, alpha, num_iters):
    #     """
    #     Performs batch gradient descent to learn w and b. Updates w and b by taking
    #     num_iters gradient steps with learning rate alpha
    #
    #     Args:
    #       X (ndarray (m,n))   : Data, m examples with n features
    #       y (ndarray (m,))    : target values
    #       w_in (ndarray (n,)) : initial model parameters
    #       b_in (scalar)       : initial model parameter
    #       alpha (float)       : Learning rate
    #       num_iters (int)     : number of iterations to run gradient descent
    #
    #     Returns:
    #       w (ndarray (n,)) : Updated values of parameters
    #       b (scalar)       : Updated value of parameter
    #       """
    #
    #     # An array to store cost J and w's at each iteration primarily for graphing later
    #     w_history = []
    #     J_history = []
    #     w = copy.deepcopy(w_in)  # avoid modifying global w within function
    #     b = b_in
    #
    #
    #
    #     converged = False
    #     for i in tqdm(range(num_iters)):
    #         if converged:
    #             break
    #
    #         # Calculate the gradient and update the parameters
    #         dj_db, dj_dw = MyML.compute_gradient(X, y, w, b)
    #
    #         # Update Parameters using w, b, alpha and gradient
    #         w = w - alpha * dj_dw
    #         b = b - alpha * dj_db
    #
    #         if i < 100000:  # prevent resource exhaustion
    #             J_history.append(MyML.compute_cost(X, y, w, b))
    #
    #         w_history.append(w)
    #
    #         converged_tmp = w
    #         a = 0
    #         if len(w_history) >= 100:
    #             for j in range(len(w_history)-1, len(w_history)-100, -1):
    #                 if (abs(converged_tmp - w_history[j]) < 0.00001).all():
    #                     continue
    #                 else:
    #                     a = 1
    #             if a == 0:
    #                 converged = True
    #
    #
    #     return w, b, J_history
