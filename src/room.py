# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, description, items=[]):
        self.room = room
        self.description = description
        self.items = items       
       
    def __str__(self):
        return f'Current location: {self.room}\n{self.description}\n Room contains: {self.contents}'
        
    def _add_item(self, item_name):
        self.items.append(item_name)

    def _remove_item(self, item_name):
        return self.items.remove(item_name)

    def __repr__(self):
        return f'{self.name} - {self.description}'
   

        
        