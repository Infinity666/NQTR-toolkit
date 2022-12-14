# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_spending_time, if you don't want an expiration: tm_stop = None
default closed_rooms = {}

init -9 python:
    from typing import Optional


    class Room(Button):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room """

        def __init__(self,
                    # Requirement
                    name: str,
                    id: str,
                    location_id: str,
                    # Room params
                    bg: str = None,
                    action_ids: Optional[list[str]] = None,
                    # Button params
                    button_icon: str = None,
                    button_icon_selected: str = None,
                    picture_in_background: str = None,
                    picture_in_background_selected: str = None,
                    xalign: int = None,
                    yalign: int = None,
                    disabled = False, # bool | str
                    hidden = False, # bool | str
                    ):
                    
            # Button init
            super().__init__(
                name= name,
                label_name= None,
                button_icon= button_icon,
                button_icon_selected= button_icon_selected,
                picture_in_background= picture_in_background,
                picture_in_background_selected= picture_in_background_selected,
                xalign= xalign,
                yalign= yalign,
                disabled= disabled,
                hidden= hidden,
            )
            # Room init
            self.id = id
            self.location_id = location_id
            self.bg = bg
            self.action_ids = self.action_ids = action_ids if action_ids else []


    class Location(Button):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location """

        def __init__(self,
                    # Requirement
                    id: str,
                    map_id: str,
                    external_room_id: str, # Will be set this room when a location is changed
                    name: str,
                    # Button params
                    button_icon: str = None,
                    button_icon_selected: str = None,
                    picture_in_background: str = None,
                    picture_in_background_selected: str = None,
                    xalign: int = None,
                    yalign: int = None,
                    disabled = False, # bool | str
                    hidden = False, # bool | str
        ):

            # Button init
            super().__init__(
                name= name,
                label_name= None,
                button_icon= button_icon,
                button_icon_selected= button_icon_selected,
                picture_in_background= picture_in_background,
                picture_in_background_selected= picture_in_background_selected,
                xalign= xalign,
                yalign= yalign,
                disabled= disabled,
                hidden= hidden,
            )
            self.id = id
            self.map_id = map_id
            self.external_room_id = external_room_id

    class Map(Button):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map """

        def __init__(self,
                    # Requirement
                    name: str,
                    bg: str,
                    map_id_north: str = None,
                    map_id_south: str = None,
                    map_id_west: str = None,
                    map_id_east: str = None,
                    disabled = False, # bool | str
                    hidden = False, # bool | str
        ):

            # Button init
            super().__init__(
                name= name,
                label_name= None,
                button_icon= None,
                button_icon_selected= None,
                picture_in_background= None,
                picture_in_background_selected= None,
                xalign= None,
                yalign= None,
                disabled= disabled,
                hidden= hidden,
            )
            self.bg = bg
            self.map_id_north = map_id_north
            self.map_id_south = map_id_south
            self.map_id_west = map_id_west
            self.map_id_east = map_id_east

    def isClosedRoom(room_id: str, closed_rooms: dict[str, Commitment], now_hour: int) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#is-closed-room """
        cur_room_is_closed = False
        closed_rooms_to_del = []
        for id, item in closed_rooms.items():
            if (id == room_id and now_is_between(start=item.tm_start, end=item.tm_stop, now=now_hour)):
                cur_room_is_closed = True
            elif (item.tm_stop != None and not now_is_between(start=item.tm_start, end=item.tm_stop, now=now_hour)):
                closed_rooms_to_del.append(id)
        for id in closed_rooms_to_del:
            del closed_rooms[id]
        del closed_rooms_to_del
        return cur_room_is_closed


    def getRoomById(room_id: str, rooms: list[Room]) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-room """
        if not room_id:
            log_warn("room_id is None", renpy.get_filename_line())
            return
        for room in rooms:
            if room.id == room_id:
                return room
        return


    def getLocationById(location_id: str, locations: list[Room]) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-location """
        if not location_id:
            log_error("location_id is None", renpy.get_filename_line())
            return
        for location in locations:
            if location.id == location_id:
                return location
        return
