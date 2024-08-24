#task 1
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {self.owner} for vehicle {self.registration_number}")

def add_vehicle(vehicles):
    reg_num = input("Enter the registration number: ")
    vehicle_type = input("Enter the vehicle type: ")
    owner = input("Enter the owner's name: ")
    vehicle = Vehicle(reg_num, vehicle_type, owner)
    vehicles[reg_num] = vehicle
    print(f"Vehicle {reg_num} added successfully!")

def update_owner(vehicles):
    reg_num = input("Enter the registration number of the vehicle to update: ")
    if reg_num in vehicles:
        new_owner = input("Enter the new owner's name: ")
        vehicles[reg_num].update_owner(new_owner)
    else:
        print(f"No vehicle found with registration number {reg_num}.")

def display_vehicles(vehicles):
    if vehicles:
        for reg_num, vehicle in vehicles.items():
            print(f"Registration Number: {vehicle.registration_number}, Type: {vehicle.type}, Owner: {vehicle.owner}")
    else:
        print("No vehicles registered.")

def vehicle_menu():
    vehicles = {}
    while True:
        print("\nVehicle Registration System Menu:")
        print("1. Add Vehicle")
        print("2. Update Owner")
        print("3. Display All Vehicles")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_vehicle(vehicles)
        elif choice == '2':
            update_owner(vehicles)
        elif choice == '3':
            display_vehicles(vehicles)
        elif choice == '4':
            print("Exiting the Vehicle Registration System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Demonstration of the Vehicle Registration System
vehicle_menu()

# task 2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added to event {self.name}. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

def event_demo():
    event1 = Event("City Marathon", "2024-09-15")

    # Adding participants
    event1.add_participant()
    event1.add_participant()

    # Retrieving the current participant count
    print(f"Total participants in {event1.name}: {event1.get_participant_count()}")

# Demonstration of the Event Management System
event_demo()
