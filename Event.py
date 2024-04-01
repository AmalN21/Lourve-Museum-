from Exhibition import Exhibition

class Event(Exhibition):
    def __init__(self, name, start_date, end_date, location, event_type, ticket_price):
        super().__init__(name, start_date, end_date, location)
        self.event_type = event_type
        self.ticket_price = ticket_price
