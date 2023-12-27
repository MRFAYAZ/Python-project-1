class Room:
    def __init__(self, room_number, capacity, status='Available'):
        self.room_number = room_number
        self.capacity = capacity
        self.status = status
        self.guest = None

class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class HotelManagementSystem:
    def __init__(self, rooms):
        self.rooms = {room.room_number: room for room in rooms}
        self.reservations = {}

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms.values() if room.status == 'Available']
        return available_rooms

    def make_reservation(self, room_number, guest):
        if room_number in self.rooms:
            room = self.rooms[room_number]
            if room.status == 'Available':
                room.status = 'Occupied'
                room.guest = guest
                self.reservations[guest.email] = room
                return f"Reservation successful for {guest.name}. Room {room_number} is now occupied by {guest.name}."
            else:
                return f"Room {room_number} is not available."
        else:
            return f"Invalid room number {room_number}."


room1 = Room(7,4)
room2 = Room(17,4)
rooms = [room1, room2]

hotel = HotelManagementSystem(rooms)

guest1 = Guest("MR FAYAZ", "fayaz@example.com", "123-456-7890")
guest2 = Guest("MS DHONI", "dhoni@example.com", "987-654-3210")

print(hotel.display_available_rooms())
print(hotel.make_reservation(17, guest1))
print(hotel.make_reservation(7, guest2))

    