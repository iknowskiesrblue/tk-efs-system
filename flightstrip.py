class FlightStrip:
    def __init__(self, callsign, aircraft_type, departure, destination, altitude, route, etd):
        self.callsign = callsign
        self.aircraft_type = aircraft_type
        self.departure = departure
        self.destination = destination
        self.altitude = altitude
        self.route = route
        self.etd = etd

    def to_dict(self):
        return {
            "Callsign": self.callsign,
            "Aircraft Type": self.aircraft_type,
            "Departure": self.departure,
            "Destination": self.destination,
            "Altitude": self.altitude,
            "Route": self.route,
            "ETD": self.etd
        }

