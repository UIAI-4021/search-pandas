import pandas as pd


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



