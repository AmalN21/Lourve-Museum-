from Artwork import Artwork
from Exhibition import Exhibition
from Event import Event
from Ticket import Ticket
from GroupTicket import GroupTicket
from Visitor import Visitor

# Create an artwork
artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Renaissance art", "Permanent Gallery")

# Create an exhibition
exhibition1 = Exhibition("Italian Renaissance", "2024-04-01", "2024-10-01", "Exhibition Hall 1")

# Create an event
event1 = Event("Light Show", "2024-05-15", "2024-05-16", "Outdoor Space", "Light and Sound", 100.0)

# Create a visitor
visitor1 = Visitor("John Doe", 35, "Adult", "AB1234567")

# Create a ticket for an exhibition
ticket1 = Ticket("T001", "2024-04-02", "2024-04-05", 63.0, visitor1.id_number, exhibition1.name)

# Create a group ticket for an event
group_ticket1 = GroupTicket("GT001", "2024-05-10", "2024-05-15", 500.0, visitor1.id_number, event1.name, 20)

# Assuming a simplified console output for demonstration
print(f"Ticket {ticket1.ticket_id} purchased for {ticket1.event_exhibition_id} by visitor {ticket1.visitor_id}")
print(f"Group ticket {group_ticket1.ticket_id} for {group_ticket1.number_of_visitors} visitors purchased for {group_ticket1.event_exhibition_id}")

