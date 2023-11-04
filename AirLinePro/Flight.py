import pandas as pd
from globals import _data_set_path

class Flight:
    def __init__(self , Airline , SourceAirport , DestinationAirport\
                 , SourceAirport_City , SourceAirport_Country , SourceAirport_Latitude\
                 , SourceAirport_Longitude , SourceAirport_Altitude , DestinationAirport_City\
                 , DestinationAirport_Country, DestinationAirport_Latitude , DestinationAirport_Longitude\
                 , DestinationAirport_Altitude , Distance , FlyTime , Price , cost):
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
        self.cost = cost

    @staticmethod
    def get_flights():
        df = pd.read_csv(_data_set_path)
        flights = list()
        for index, record in df.iterrows():
            primary_pow = 10 ** 3
            # cost = 6 * record['Price'] + 3 * record['FlyTime'] + record['Distance']   #kianoosh`s way
            cost = record['Distance'] * primary_pow + record['FlyTime'] * primary_pow * (10 ** 2) + \
                   record['Price'] * primary_pow * (10 ** 2) * (10 ** 3)  # melika`s way

            f = Flight(record['Airline'], record['SourceAirport'], record['DestinationAirport']
                       , record['SourceAirport_City'], record['SourceAirport_Country']
                       , record['SourceAirport_Latitude'], record['SourceAirport_Longitude']
                       , record['SourceAirport_Altitude'], record['DestinationAirport_City']
                       , record['DestinationAirport_Country'], record['DestinationAirport_Latitude']
                       , record['DestinationAirport_Longitude'], record['DestinationAirport_Altitude']
                       , record['Distance'], record['FlyTime'], record['Price'], cost)

            flights.append(f)
        return flights

