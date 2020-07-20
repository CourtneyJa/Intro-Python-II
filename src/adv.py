import sys
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

#items
item = {
    'sword' : Item('Sword', 'Sword of Omens'),
    'lamp' : Item('Lamp', 'long burning oil lamp'),
    'coins' : Item('Gold', 'a pound of gold coins'),
    'metal' : Item('Metal', 'iron to make a new sword'),
    'meat' : Item('Meat', 'leg of lamb'),
    'map' : Item('Atlas of Lands', 'map of the worlds')
}

#items to rooms:
room['outside'].items.append(item['lamp'])
room['foyer'].items.append(item['meat'])
room['overlook'].items.append(item['sword'])
room['narrow'].items.append(item['metal'])
room['treasure'].items.append(item['coins'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

actions = {
    'cardinals': ['n', 's', 'e', 'w'],
    'play_act': ['on_grab', 'on_drop'],
    'quit': ['q']
}

def start_play():
    running = True 
    add_name = input('Brave hero, please enter your name')    
    player1 = Player(add_name, room['outside'])  

    print(
        f'Welcome {player1.name}!\nGet started on your quest\nuse [n] [s] [e] [w] to move player')
    while (running is not False):
        player1._show_current_room()

        add_name = input(
            'Choose your next move\n >> ')

        if add_name in actions['cardinals']:
            player1._move(add_name)

        if add_name in actions['quit']:
            running = False
            print('You have quit the game. Goodbye!')

if __name__ == "__main__":
    start_play()
