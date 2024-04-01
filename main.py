from Exhibition import Exhibition
from Event import Event
from Artwork import Artwork
from Ticket import Ticket
from GroupTicket import GroupTicket
from Visitor import Visitor
from MuseumLocation import MuseumLocation

# Sample data collections for simplicity
museum_locations = []
exhibitions = []
events = []
artworks = []
tickets = []
visitors = []

def display_menu():
    print("\nWelcome to the Louvre Abu Dhabi Management System")
    print("1. Purchase Ticket")
    print("2. Add/Edit Exhibition")
    print("3. Add/Edit Artwork")
    print("4. Add/Edit Special Event")
    print("5. Manage Museum Locations")
    print("6. Exit")

def purchase_ticket():
    print("\nPurchase Ticket")
    print("1. Exhibition")
    print("2. Special Event")
    choice = input("Select the type of ticket you want to purchase (1-2): ")

    if choice == "1":
        for index, exhibition in enumerate(exhibitions, start=1):
            print(f"{index}. {exhibition.name} (Start: {exhibition.start_date}, End: {exhibition.end_date})")
    elif choice == "2":
        for index, event in enumerate(events, start=1):
            print(f"{index}. {event.name} - {event.event_type} (Start: {event.start_date}, End: {event.end_date}, Price: {event.ticket_price} AED)")
    else:
        print("Invalid choice.")
        return

    selection = int(input("Select the number of the exhibition/event: ")) - 1
    if choice == "1" and selection >= 0 and selection < len(exhibitions):
        selected_exhibition_event = exhibitions[selection]
    elif choice == "2" and selection >= 0 and selection < len(events):
        selected_exhibition_event = events[selection]
    else:
        print("Invalid selection.")
        return

    visitor_name = input("Enter your name: ")
    visitor_age = int(input("Enter your age: "))
    visitor_type = "Adult" if visitor_age > 18 and visitor_age < 60 else "Concession"
    visitor_id = input("Enter your ID number: ")

    visitor = Visitor(visitor_name, visitor_age, visitor_type, visitor_id)
    visitors.append(visitor)

    is_group = input("Is this a group ticket purchase? (yes/no): ").lower() == "yes"
    if is_group:
        number_of_visitors = int(input("Enter the number of visitors: "))
        total_price = (selected_exhibition_event.ticket_price if choice == "2" else 63) * number_of_visitors
        if number_of_visitors >= 15:
            total_price *= 0.5  # Apply group discount
    else:
        total_price = selected_exhibition_event.ticket_price if choice == "2" else 63

    # Assuming all tickets have a flat 5% VAT applied
    total_price *= 1.05

    ticket_id = f"T{len(tickets)+1}"
    if is_group:
        ticket = GroupTicket(ticket_id, "Purchase Date Placeholder", "Event Date Placeholder", total_price, visitor_id, selected_exhibition_event.name, number_of_visitors)
    else:
        ticket = Ticket(ticket_id, "Purchase Date Placeholder", "Event Date Placeholder", total_price, visitor_id, selected_exhibition_event.name)
    tickets.append(ticket)

    print(f"Ticket purchased successfully! Total Price: {total_price} AED")


def add_edit_exhibition():
    print("\nAdd/Edit Exhibition")
    action = input("Do you want to add a new exhibition or edit an existing one? (add/edit): ").lower()

    if action == "add":
        name = input("Enter exhibition name: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        print("Available locations:")
        for location in museum_locations:
            print(f"{location.location_id}: {location.name}")

        location = input("Enter location: ")

        if not any(location.location_id == location for location in museum_locations):
            print("Location not found.")
            return



        # Create a new Exhibition object and add it to the exhibitions list
        new_exhibition = Exhibition(name,  start_date, end_date, museum_locations[location])
        exhibitions.append(new_exhibition)
        print("Exhibition added successfully!")
    elif action == "edit":
        name_to_edit = input("Enter the name of the exhibition you want to edit: ")
        # Find the exhibition by name
        exhibition = next((ex for ex in exhibitions if ex.name == name_to_edit), None)

        if exhibition:
            # Assuming you want to allow editing of all details except the name
            new_start_date = input(f"Enter new start date (YYYY-MM-DD) ({exhibition.start_date}): ")
            new_end_date = input(f"Enter new end date (YYYY-MM-DD) ({exhibition.end_date}): ")
            new_location = input(f"Enter new location ({exhibition.location}): ")

            # Update the exhibition details
            exhibition.start_date = new_start_date if new_start_date else exhibition.start_date
            exhibition.end_date = new_end_date if new_end_date else exhibition.end_date
            exhibition.location = new_location if new_location else exhibition.location

            print("Exhibition edited successfully!")
        else:
            print("Exhibition not found.")
    else:
        print("Invalid action.")


def add_edit_artwork():
    print("\nAdd/Edit Artwork")
    action = input("Do you want to add a new artwork or edit an existing one? (add/edit): ").lower()

    if action == "add":
        title = input("Enter artwork title: ")
        artist = input("Enter artist name: ")
        creation_date = input("Enter creation date (YYYY-MM-DD): ")
        historical_significance = input("Enter historical significance: ")
        print("Available locations:")
        for location in museum_locations:
            print(f"{location.location_id}: {location.name}")
        location = input("Enter location ID: ")

        if not any(location.location_id == location for location in museum_locations):
            print("Location not found.")
            return

        # Create a new Artwork object and add it to the artworks list
        new_artwork = Artwork(title, artist, creation_date, historical_significance, museum_locations[location])
        artworks.append(new_artwork)
        print("Artwork added successfully!")
    elif action == "edit":
        title_to_edit = input("Enter the title of the artwork you want to edit: ")
        # Find the artwork by title
        artwork = next((art for art in artworks if art.title == title_to_edit), None)

        if artwork:
            # Assuming you want to allow editing of all details except the title
            new_artist = input(f"Enter new artist name ({artwork.artist}): ")
            new_creation_date = input(f"Enter new creation date (YYYY-MM-DD) ({artwork.creation_date}): ")
            new_historical_significance = input(f"Enter new historical significance ({artwork.historical_significance}): ")
            print("Available locations:")
            for location in museum_locations:
                print(f"{location.location_id}: {location.name}")

            new_location = input(f"Enter new location ID:")
            if not any(location.location_id == new_location for location in museum_locations):
                print("Location not found.")
                return

            # Update the artwork details
            artwork.artist = new_artist if new_artist else artwork.artist
            artwork.creation_date = new_creation_date if new_creation_date else artwork.creation_date
            artwork.historical_significance = new_historical_significance if new_historical_significance else artwork.historical_significance
            artwork.location = new_location if new_location else artwork.location

            print("Artwork edited successfully!")
        else:
            print("Artwork not found.")
    else:
        print("Invalid action.")

def add_edit_event():
    print("\nAdd/Edit Special Event")
    action = input("Do you want to add a new event or edit an existing one? (add/edit): ").lower()

    if action == "add":
        name = input("Enter event name: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        print("Available locations:")
        for location in museum_locations:
            print(f"{location.location_id}: {location.name}")

        location = input(f"Enter new location ID:")
        if not any(location.location_id == new_location for location in museum_locations):
            print("Location not found.")
            return

        location = input("Enter location: ")
        event_type = input("Enter event type: ")
        ticket_price = float(input("Enter ticket price: "))

        # Create a new Event object and add it to the events list
        new_event = Event(name, start_date, end_date, location, event_type, ticket_price)
        events.append(new_event)
        print("Event added successfully!")
    elif action == "edit":
        name_to_edit = input("Enter the name of the event you want to edit: ")
        # Find the event by name
        event = next((ev for ev in events if ev.name == name_to_edit), None)

        if event:
            # Assuming you want to allow editing of all details except the name
            new_start_date = input(f"Enter new start date (YYYY-MM-DD) ({event.start_date}): ")
            new_end_date = input(f"Enter new end date (YYYY-MM-DD) ({event.end_date}): ")
            print("Available locations:")
            for location in museum_locations:
                print(f"{location.location_id}: {location.name}")

            new_location = input(f"Enter new location ID:")
            if not any(location.location_id == new_location for location in museum_locations):
                print("Location not found.")
                return
            new_location = input(f"Enter new location ({event.location}): ")
            new_event_type = input(f"Enter new event type ({event.event_type}): ")
            new_ticket_price = float(input(f"Enter new ticket price ({event.ticket_price}): "))

            # Update the event details
            event.start_date = new_start_date if new_start_date else event.start_date
            event.end_date = new_end_date if new_end_date else event.end_date
            event.location = new_location if new_location else event.location
            event.event_type = new_event_type if new_event_type else event.event_type
            event.ticket_price = new_ticket_price if new_ticket_price else event.ticket_price

            print("Event edited successfully!")
        else:
            print("Event not found.")
    else:
        print("Invalid action.")

def manage_museum_locations():
    print("\nManage Museum Locations")
    # Option to add a new location or edit an existing one
    action = input("Do you want to (A)dd a new location or (E)dit an existing one? (A/E): ").lower()
    if action == 'a':
        location_id = input("Enter location ID: ")
        name = input("Enter location name: ")
        description = input("Enter location description: ")
        new_location = MuseumLocation(location_id, name, description)
        museum_locations.append(new_location)
        print("New museum location added successfully.")
    elif action == 'e':
        # Simplified edit logic for demonstration purposes
        location_id = input("Enter the location ID to edit: ")
        # Find and edit the location if it exists
        print("Location edited successfully.")
    else:
        print("Invalid action.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            purchase_ticket()
        elif choice == "2":
            add_edit_exhibition()
        elif choice == "3":
            add_edit_artwork()
        elif choice == "4":
            add_edit_event()
        elif choice == "5":
            manage_museum_locations()
            break
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
