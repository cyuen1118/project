



from flight import Flight

class Airline:
    def __init__(self, name):
        self._name = name
        self._flights = []

    def add_flight(self, flight):
        self._flights.append(flight)

    def get_flight(self):
        return self._flights

    def display_airline(self):
        return f"Airline: {self._name}"


