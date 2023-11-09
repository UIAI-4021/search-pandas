import pandas as pd
class MyML:

    @staticmethod
    def label_encode(flight_price_df):
        time_mapping = {
            'Early_Morning' : 1,
            'Morning' : 2,
            'Afternoon' : 3,
            'Evening' : 4,
            'Night' : 5,
            'Late_Night' : 6
        }

        stops_mapping = {
            'zero' : 1,
            'one' : 2,
            'two_or_more' : 3
        }
        class_mapping = {
            'Economy' : 1,
            'Business' : 2
        }

        flight_price_df['departureTimeMapping'] = flight_price_df['departure_time'].map(time_mapping)
        flight_price_df['arrivalTimeMapping'] = flight_price_df['arrival_time'].map(time_mapping)
        flight_price_df['stopsMapping'] = flight_price_df['stops'].map(stops_mapping)
        flight_price_df['classMapping'] = flight_price_df['class'].map(class_mapping)
