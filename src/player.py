# Write a class to hold player information, e.g. what room they are in
# current
from room import Room

cardinals = {
    'n': 'North',
    's': 'South',
    'w': 'West',
    'e': 'East'
}

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def walk(self, direction):
        if direction in [cardinals]:
            new_room= self.current_room.get_direction(direction)
            if new_room is not None:
                self.current_room = new_room
                print(self.current_room)
            else:
                print('Player is stuck, make a new choice')