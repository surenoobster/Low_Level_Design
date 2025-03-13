class Room:
    def __init__(self, room_number):
        self.room_number = room_number

    def print_room( room_number):
        print(f"printing my room no. {room_number}")

class House:
    def __init__(self, room_number):
        self.room = Room(room_number)  # Composition

    def show_details(self):
        print(f"House has Room number: {self.room.room_number}")


room_mine = Room(101)
room_mine_2 = Room.print_room(109)
my_house = House(101)
my_house.show_details()



#or

class Room:
    def __init__(self, room_number):
        self.room_number = room_number

    def print_room(self):
        print(f"printing my room no. {self.room_number}")

room_mine = Room(101)
room_mine.print_room()  # This will work
