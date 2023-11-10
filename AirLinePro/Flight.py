import pandas as pd
from globals import _data_set_path
from globals import _flight_price_dataset
from MachineLearning import MyML
class Flight:
    def __init__(self, Airline, SourceAirport, DestinationAirport
                 , SourceAirport_City, SourceAirport_Country, SourceAirport_Latitude
                 , SourceAirport_Longitude, SourceAirport_Altitude, DestinationAirport_City
                 , DestinationAirport_Country, DestinationAirport_Latitude, DestinationAirport_Longitude
                 , DestinationAirport_Altitude, Distance, FlyTime, Price, Cost):
        self.Airline = Airline
        self.SourceAirport = SourceAirport
        self.DestinationAirport = DestinationAirport
        self.SourceAirport_City = SourceAirport_City
        self.SourceAirport_Country = SourceAirport_Country
        self.SourceAirport_Latitude = SourceAirport_Latitude
        self.SourceAirport_Longitude = SourceAirport_Longitude
        self.SourceAirport_Altitude = SourceAirport_Altitude
        self.DestinationAirport_City = DestinationAirport_City
        self.DestinationAirport_Country = DestinationAirport_Country
        self.DestinationAirport_Latitude = DestinationAirport_Latitude
        self.DestinationAirport_Longitude = DestinationAirport_Longitude
        self.DestinationAirport_Altitude = DestinationAirport_Altitude
        self.Distance = Distance
        self.FlyTime = FlyTime
        self.Price = Price
        self.Cost = Cost

    @staticmethod
    def get_cost(record):
        # cost = 6 * record['Price'] + 3 * record['FlyTime'] + record['Distance']   #kianoosh`s way
        primary_pow = 10 ** 3
        cost = record['Distance'] * primary_pow + record['FlyTime'] * primary_pow * (10 ** 2) + \
               record['Price'] * primary_pow * (10 ** 2) * (10 ** 3)  # melika`s way
        return cost

    @staticmethod
    def get_flights():
        df = pd.read_csv(_data_set_path)
        flights = list()
        for index, record in df.iterrows():
            cost = Flight.get_cost(record)

            f = Flight(record['Airline'], record['SourceAirport'], record['DestinationAirport']
                       , record['SourceAirport_City'], record['SourceAirport_Country']
                       , record['SourceAirport_Latitude'], record['SourceAirport_Longitude']
                       , record['SourceAirport_Altitude'], record['DestinationAirport_City']
                       , record['DestinationAirport_Country'], record['DestinationAirport_Latitude']
                       , record['DestinationAirport_Longitude'], record['DestinationAirport_Altitude']
                       , record['Distance'], record['FlyTime'], record['Price'], cost)

            flights.append(f)
        return flights





class FlightPrice:
    def __init__(self , departure_time, stops, arrival_time, flight_class,
                        duration, days_left, price,
                        departure_time_mapping,
                        arrival_time_mapping,
                        stops_mapping,
                        class_mapping,
                 ):
        self.departure_time = departure_time
        self.stops = stops
        self.arrival_time = arrival_time
        self.flight_class = flight_class
        self.duration = duration
        self.days_left = days_left
        self.price = price

        self.departure_time_mapping = departure_time_mapping
        self.arrival_time_mapping = arrival_time_mapping
        self.stops_mapping = stops_mapping
        self.class_mapping = class_mapping

    @staticmethod
    def set_df(df):
        df = df
    @staticmethod
    def get_flights_price():
        df = pd.read_csv(_flight_price_dataset)
        MyML.label_encode(df)
        flights_price = list()
        # for index, record in df.iterrows():
        #
        #     f = FlightPrice(record['departure_time'], record['stops'], record['arrival_time'],
        #                     record['class'], record['duration'],
        #                     record['days_left'], record['price'],
        #                     record['departureTimeMapping'], record['arrivalTimeMapping'],
        #                     record['stopsMapping'], record['classMapping'])
        #
        #     flights_price.append(f)
        return df
