




class Flight:
    def __init__(self, flight_number, origin, destination, capacity):
        self._flight_number = flight_number
        self._origin = origin
        self._destination = destination
        self._capacity = capacity
        self._passengers = []

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number
    
    def get_flight_number(self):
        return self._flight_number

    def set_origin(self, origin):
        self._origin = origin 
    
    def get_origin(self):
        return self._origin
    
    def set_destination(self, destination):    
        self._destination = destination
        
    def get_destination(self):
        return self._destination 

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_capacity(self):
        return self._capacity

    def add_passenger(self, passenger):
        if len(self._passengers) < self._capacity:
            self._passengers.append(passenger)
        return False

    def get_passengers(self):
        return self._passengers

    def display_flight(self):
        return f"Flight no: {self._flight_number}, origin: {self._origin}, destination: {self._destination}, capacity: {self._capacity}"


