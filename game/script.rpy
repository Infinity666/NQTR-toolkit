﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alice")


# The game starts here.

label start:

    $ cur_location = "house"
    $ cur_room = rooms[0]
    $ prev_room = rooms[5]
    $ updateBL()
    scene expression (cur_room.bg)

    call screen room_navigation

    return
