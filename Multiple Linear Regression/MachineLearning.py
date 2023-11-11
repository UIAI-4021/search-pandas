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

        df_encoded = pd.get_dummies(flight_price_df, columns=['departure_time', 'arrival_time', 'stops', 'class'], drop_first=True)
        return df_encoded
    @staticmethod
    def scaler(flight_price_df):
        flight_price_df = pd.DataFrame(flight_price_df)
        scaler = StandardScaler()
        flight_price_df['days_left'] = scaler.fit_transform(flight_price_df['days_left'].values.reshape(-1,1))
        flight_price_df['duration'] = scaler.fit_transform(flight_price_df['duration'].values.reshape(-1,1))

    @staticmethod
    def split(flight_price_df):

        x_train, x_test, y_train, y_test = train_test_split(
            np.array(flight_price_df.drop('price', axis=1)),
            np.array(flight_price_df['price']),
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

        tmp_num_iters = 20100
        converged = False
        for i in tqdm(range(tmp_num_iters), desc='Training', unit='record'):
            if converged:
                break

            dj_db, dj_dw = MyML.compute_gradient(X, y, w, b)

            w -= alpha * dj_dw
            b -= alpha * dj_db

            if i < 100000:
                J_history.append(MyML.compute_cost(X, y, w, b))
            w_history.append(w)

            if len(w_history) >= 20000:
                for j in range(len(w_history)-1, len(w_history)-100, -1):
                    if np.allclose(w_history[-1], w_history[j], atol=1e-10000):
                        continue
                    else:
                        break
                else:
                    converged = True


        return w, b, J_history

    @staticmethod
    def calculate_error(y_true, y_pred):
        Y_true = np.array(copy.copy(y_true))
        Y_pred = np.array(copy.copy(y_pred))

        scaler = StandardScaler()

        Y_true = scaler.fit_transform(Y_true.reshape(-1,1))
        Y_pred = scaler.fit_transform(Y_pred.reshape(-1,1))

        # MAE
        mae = mean_absolute_error(Y_true, Y_pred)
        # MSE
        mse = mean_squared_error(Y_true, Y_pred)
        # RMSE
        rsme = math.sqrt(mse)
        # R2
        r2 = r2_score(Y_true, Y_pred)

        return mae, mse, rsme, r2

        # print(f'MAE: {mae}, MSE: {mse}, RMSE: {rsme}, R2: {r2}')

