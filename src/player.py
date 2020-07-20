# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def _show_current_room(self):
        print(
            f'Current location: {self.current_room.room}\n Description: {self.current_room.description}')

    def _show_options(self):
        print(
            f'\nTo move enter: [n] North [s] South [e] East [w] West or [q] Quit\n')

    def _move(self, direction_input):
        try:
            self.current_room = self.current_room.__getattribute__(
                f'{direction_input}_to')
        except:
            print(
                '\nPlayer is stuck, please make another choice\n')

    def on_grab(self, item_name):
        try:
            if item_name in self.current_room.items:
                new_item = self.current_room._remove_item(item_name)
                self.inventory.append(new_item)
                print(f'You have selected {new_item}.')
        except:
            print(f'{item_name} cannot be added to inventory')

    def on_drop(self, item_name):
        try:
            if item_name in self.inventory:
                dropped_item = self.inventory.remove(item_name)
                self.current_room._add_item(dropped_item)
                print(f'{item_name} has been dropped')
        except:
            print(f'{item_name} is required item, cannot be dropped')

    def __str__(self):
        return f'Current location: {self.current_room}'

    def __repr__(self):
        return f'Player({self.name}, {self.current_room})'