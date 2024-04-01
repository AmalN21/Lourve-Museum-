from Ticket import Ticket

class GroupTicket(Ticket):
    def __init__(self, ticket_id, purchase_date, event_date, price, visitor_id, event_exhibition_id, number_of_visitors):
        super().__init__(ticket_id, purchase_date, event_date, price, visitor_id, event_exhibition_id)
        self.number_of_visitors = number_of_visitors
        self.discount_applied = True if number_of_visitors >= 15 else False
