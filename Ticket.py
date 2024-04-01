class Ticket:
    def __init__(self, ticket_id, purchase_date, event_date, price, visitor_id, event_exhibition_id):
        self.ticket_id = ticket_id
        self.purchase_date = purchase_date
        self.event_date = event_date
        self.price = price
        self.visitor_id = visitor_id
        self.event_exhibition_id = event_exhibition_id
