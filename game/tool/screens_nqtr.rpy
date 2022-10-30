image gui triangular_button = "/interface/button/triangular_button.webp"
# Id of the task selected in the menu
default cur_task_menu = ""
# quest level based on the task selected in the menu
default cur_quest_menu = ""

screen room_navigation():
    modal True
    $ i = 0
    # More information by hovering the mouse
    $ (x,y) = renpy.get_mouse_pos()

    # Map
    if (map_open and cur_map_id):
        $ map_id_north = maps[cur_map_id].map_id_north
        $ map_id_south = maps[cur_map_id].map_id_south
        $ map_id_east = maps[cur_map_id].map_id_east
        $ map_id_west = maps[cur_map_id].map_id_west

        # North map
        if (not isNullOrEmpty(map_id_north) and not maps[map_id_north].isHidden()):
            hbox:
                align (0.5, 0.1)
                imagebutton:
                    idle "gui triangular_button"
                    focus_mask True
                    sensitive not maps[map_id_north].isDisabled()
                    action [
                        SetVariable('cur_map_id', map_id_north), 
                        Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                    ]
                    if renpy.variant("pc"):
                        tooltip maps[map_id_north].name
                    at middle_map(rotation = 270)
        # South map
        if (not isNullOrEmpty(map_id_south) and not maps[map_id_south].isHidden()):
            hbox:
                align (0.5, 0.99)
                imagebutton:
                    idle "gui triangular_button"
                    focus_mask True
                    sensitive not maps[map_id_south].isDisabled()
                    action [
                        SetVariable('cur_map_id', map_id_south), 
                        Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                    ]
                    if renpy.variant("pc"):
                        tooltip maps[map_id_south].name
                    at middle_map(rotation = 90)
        # West map
        if (not isNullOrEmpty(map_id_west) and not maps[map_id_west].isHidden()):
            hbox:
                align (0.001, 0.5)
                imagebutton:
                    idle "gui triangular_button"
                    focus_mask True
                    sensitive not maps[map_id_west].isDisabled()
                    action [
                        SetVariable('cur_map_id', map_id_west), 
                        Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                    ]
                    if renpy.variant("pc"):
                        tooltip maps[map_id_west].name
                    at middle_map(rotation = 180)
        # East map
        if (not isNullOrEmpty(map_id_east) and not maps[map_id_east].isHidden()):
            hbox:
                align (0.999, 0.5)
                imagebutton:
                    idle "gui triangular_button"
                    focus_mask True
                    sensitive not maps[map_id_east].isDisabled()
                    action [
                        SetVariable('cur_map_id', map_id_east), 
                        Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                    ]
                    if renpy.variant("pc"):
                        tooltip maps[map_id_east].name
                    at middle_map(rotation = 0)

        for location in locations:
            # If the Map where I am is the same as the Map where the room is located
            if (location.map_id == cur_map_id and not location.isHidden()):
                vbox:
                    align (location.yalign, location.xalign)
                    imagebutton:
                        idle location.getPictureInBackgroundOrDefault()
                        selected_idle location.getSelectedPictureInBackgroundOrDefault()
                        selected_hover location.getSelectedPictureInBackgroundOrDefault()
                        selected location == cur_location
                        sensitive not location.isHidden()
                        focus_mask True
                        action [
                            SetVariable('cur_location', location),
                            Call("after_return_from_room_navigation", label_name_to_call = "change_location"),
                        ]
                        at small_map

                    # Locations name
                    text location.name:
                        font 'DejaVuSans.ttf'
                        size 18
                        drop_shadow [(2, 2)]
                        xalign 0.5
                        text_align 0.5
                        line_leading 0
                        line_spacing -2

    else:
        # Rooms
        hbox:
            yalign 0.99
            xalign 0.01
            spacing 2

            for room in rooms:
                $ i += 1

                # If the Locations where I am is the same as the Locations where the room is located
                if (room.location_id == cur_location.id and room.isButton() != None and not room.isHidden()):
                    button:
                        xysize (126, 190)
                        action [
                            SetVariable('prev_room', cur_room),
                            SetVariable('cur_room', room),
                            Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                        ]
                        has vbox xsize 126 spacing 0

                        frame:
                            xysize (126, 140)
                            background None

                            # Room icon
                            imagebutton:
                                align (0.5, 0.0)
                                idle room.getButtonOrDefault()
                                selected_idle room.getSelectedButtonOrDefault()
                                selected_hover room.getSelectedButtonOrDefault()
                                selected (True if cur_room and cur_room.id == room.id else False)
                                sensitive not room.isDisabled()
                                focus_mask True
                                action [
                                    SetVariable('prev_room', cur_room),
                                    SetVariable('cur_room', room),
                                    Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                                ]
                                at middle_room

                            # Check the presence of ch in that room
                            $ there_are_ch = False
                            for comm in commitments_in_cur_location.values():
                                # If it is the selected room
                                if comm != None and room.id == comm.room_id:
                                    # I insert hbox only if they are sure that someone is there
                                    $ there_are_ch = True

                            if there_are_ch:
                                hbox:
                                    ypos 73
                                    xalign 0.5
                                    spacing - 30

                                    for comm in commitments_in_cur_location.values():
                                        # If it is the selected room
                                        if room.id == comm.room_id:
                                            for ch_icon in comm.getChIcons(ch_icons):
                                                imagebutton:
                                                    idle ch_icon
                                                    sensitive not room.isDisabled()
                                                    focus_mask True
                                                    action [
                                                        SetVariable('prev_room', cur_room),
                                                        SetVariable('cur_room', room),
                                                        Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                                                    ]
                                                    at small_face

                        # Room name
                        text room.name:
                            font 'DejaVuSans.ttf'
                            size 18
                            drop_shadow [(2, 2)]
                            xalign 0.5
                            text_align 0.5
                            line_leading 0
                            line_spacing -2
                    key str(i) action [
                        SetVariable('prev_room', cur_room),
                        SetVariable('cur_room', room),
                        Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                    ]

        # Action wich Picture in background
        for room in rooms:
            # Adds the button list of possible actions in that room
            if (cur_room and room.id == cur_room.id and not room.id in closed_rooms):
                # actions: dict[str, Act], room: Room,  now_is_between: callable[[int, int], bool], cur_day: int
                for act in getActions(actions= actions | df_actions, room = room, now_hour = tm.get_hour_number() , cur_day = tm.get_day_number()):
                    if (not act.isButton()):
                        imagebutton:
                            align (act.xalign, act.yalign)
                            idle act.getPictureInBackgroundOrDefault()
                            hover act.getSelectedPictureInBackgroundOrDefault()
                            focus_mask True
                            action [
                                Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
                            ]
                            if renpy.variant("pc"):
                                tooltip act.name
                            at middle_action_is_in_room
        # Normal Actions (with side button)
        vbox:
            yalign 0.95
            xalign 0.99
            for room in rooms:
                # Adds the button list of possible actions in that room
                if (cur_room and room.id == cur_room.id):
                    for act in getActions(actions= actions | df_actions, room = room, now_hour = tm.get_hour_number() , cur_day = tm.get_day_number()):
                        if (act.isButton() == True and not act.isHidden()):
                            imagebutton:
                                idle act.getButtonOrDefault()
                                hover act.getSelectedButtonOrDefault()
                                focus_mask True
                                action [
                                    Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
                                ]
                                if renpy.variant("pc"):
                                    tooltip act.name
                                at middle_action

                # Talk
                # Adds a talk for each ch (NPC) and at the talk interval adds the icon for each secondary ch
                for comm in commitments_in_cur_location.values():
                    if (cur_room and comm and room.id == comm.room_id and room.id == cur_room.id):
                        # Insert in talk for every ch, main in that room
                        for ch_id, talk_obj in comm.ch_talkobj_dict.items():
                            if (not talk_obj.isHidden()):
                                frame:
                                    xysize (120, 120)
                                    background None

                                    imagebutton:
                                        idle talk_obj.getButtonIcon()
                                        hover talk_obj.getSelectedButtonOrDefault()
                                        focus_mask True
                                        action [
                                            SetVariable('talk_ch', ch_id),
                                            SetVariable('talk_image', comm.getTalkBackground(ch_id)),
                                            Call("after_return_from_room_navigation", label_name_to_call = talk_obj.getTalkLabelName()),
                                        ]
                                        at middle_action
                                    # inserts the icon of the character who is currently in that room
                                    # TODO: for now insert only the icon of the main ch_id, I have to insert also the icon of the other secondary ch_id
                                    if (ch_id in ch_icons):
                                        imagebutton:
                                            idle ch_icons.get(ch_id)
                                            focus_mask True
                                            at small_face
                                            action [
                                                SetVariable('talk_ch', ch_id),
                                                SetVariable('talk_image', comm.getTalkBackground(ch_id)),
                                                Call("after_return_from_room_navigation", label_name_to_call = talk_obj.getTalkLabelName()),
                                            ]
                                    if renpy.variant("pc"):
                                        tooltip _("Talk")

            # Fixed button to wait
            imagebutton:
                idle '/interface/action-wait.webp'
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "wait"),
                ]
                if renpy.variant("pc"):
                    tooltip _("Wait")
                at middle_action

    # Time
    hbox:
        align (0.5, 0.01)
        vbox:
            align (0.5, 0.01)
            text "[tm.hour]:00":
                xalign (0.5)
                font 'DejaVuSans.ttf'
                size 60
                drop_shadow [(2, 2)]
            text tm.get_weekday_name():
                xalign (0.5)
                font 'DejaVuSans.ttf'
                size 24
                drop_shadow [(2, 2)]
                line_leading -16

        if (map_open):
            # Fixed button to wait
            imagebutton:
                xysize (300, 300)
                idle '/interface/action-wait.webp'
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "wait"),
                ]
                if renpy.variant("pc"):
                    tooltip _("Wait")
                at middle_action

    # Tools
    hbox:
        align (0.01, 0.01)
        spacing 2

        imagebutton:
            idle '/interface/menu-options.webp'
            focus_mask True
            action ShowMenu('save')
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Settings")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-user.webp'
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = "development_characters_info"),
            ]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Characters info")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-memo.webp'
            focus_mask True
            if len(current_quest_stages) > 0 :
                action [
                    Show('menu_memo'),
                ]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Memo")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-help.webp'
            focus_mask True
            action ShowMenu('help')
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Help")
            else:
                at small_menu_mobile

    hbox:
        align (0.99, 0.01)
        spacing 2

        # Money
        text "$20":
            align(1.0, 0.5)
            font 'DejaVuSans.ttf'
            size 30
            drop_shadow [(2, 2)]

        imagebutton:
            idle '/interface/menu-inventory.webp'
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = "development_inventory"),
            ]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Backpack")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-phone.webp'
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = "development"),
            ]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Smartphone")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-map.webp'
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = "open_map"),
            ]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Map")
            else:
                at small_menu_mobile

    # More information by hovering the mouse
    if renpy.variant("pc"):
        $ text = GetTooltip()
        if text:
            text "[text]":
                xpos x-20
                ypos y-20
                font 'DejaVuSans.ttf' 
                size 18 
                drop_shadow [(2, 2)] 
                outlines [(2, "#000", 0, 1)]

screen menu_memo():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"
    add "gui/overlay/game_menu.png"

    frame area (150, 70, 350, 50) background None:
        text _("{b}Memo{/b}") color gui.accent_color size gui.name_text_size

    # Synchronize number_stages_completed_in_quest with quests
    $ updateQuestsLevels()

    # button for closure
    imagebutton:
        align (0.95, 0.05)
        idle '/interface/button/close_idle.webp'
        action [
            Hide('menu_memo'),
        ]
        if renpy.variant("pc"):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_mobile

    frame:
        ypos 170
        xpos 80
        xsize 400
        ysize 850
        background None
        # task title list
        viewport mousewheel 'change' draggable True id 'vp1':
            has vbox spacing 5
            for task_id in current_quest_stages.keys():
                button:
                    xpos 30
                    xsize 390
                    background None
                    action [
                        SetVariable('cur_task_menu', task_id),
                        SetVariable('cur_quest_menu', number_stages_completed_in_quest[task_id])
                    ]
                    xpadding 0
                    ypadding 0
                    xmargin 0
                    ymargin 0
                    textbutton quests[task_id].title:
                        action [
                            SetVariable('cur_task_menu', task_id),
                            SetVariable('cur_quest_menu', number_stages_completed_in_quest[task_id]),
                        ]
                        selected cur_task_menu == task_id
        # scroll bar
        vbar value YScrollValue('vp1') style 'menu_vscroll'

    # Information on the current quest
    if cur_task_menu != '':
        $ quest_menu = quest_stages[quests[cur_task_menu].stages_id[cur_quest_menu]]
        vbox:
            align (0.72, 0.6)
            # Image
            if quest_menu.bg != '' and quest_menu.bg != None:
                add Frame(quest_menu.bg, Borders(0,0,0,0)):
                    xsize 800
                    ysize 400
                    pos (195,0)
            elif quests[cur_task_menu].bg != '' and quests[cur_task_menu].bg != None:
                add Frame(quests[cur_task_menu].bg, Borders(0,0,0,0)):
                    xsize 800
                    ysize 400
                    pos (195,0)
            frame:
                xsize 1180
                xalign 0.5
                background None

                text quest_menu.title:
                    size 30
                    font 'DejaVuSans.ttf'
                    xalign 0.5

            frame:
                area (0, 0, 1190, 400)
                background None

                has hbox
                viewport mousewheel 'change' draggable True id 'vp2':
                    has vbox spacing 30
                    if cur_task_menu in quests_descriptions:
                        text quests_descriptions[cur_task_menu] size 24 color gui.accent_color
                    else:
                        text quests[cur_task_menu].description size 24 color gui.accent_color
                    if (current_quest_stages[cur_task_menu].active):
                        text quest_menu.description size 24
                        text quest_menu.advice size 28
                        for item in quest_menu.goals:
                            text item.description size 28
                        if current_quest_stages[cur_task_menu].completed and (cur_quest_menu+1) == len(quests[cur_task_menu].stages_id):
                            if quests[cur_task_menu].development:
                                text _("It is currently the end of this story, unfortunately you have to wait for an update to continue this story.") size 28
                            else:
                                text _("You have completed all the quests.") size 28
                    else:
                        text quest_menu.request_description size 24 color gui.accent_color
                vbar value YScrollValue('vp2') style 'menu_vscroll'

    if (cur_task_menu != '' and number_stages_completed_in_quest[cur_task_menu] > 0):
        # increases and decreases cur_quest menu
        imagebutton align (680/1920, 340/1080):
            idle '/interface/button/prev_idle.webp'
            hover '/interface/button/prev_hover.webp'
            insensitive '/interface/button/prev_insensitive.webp'
            focus_mask True
            sensitive (cur_quest_menu > 0)
            action [
                SetVariable('cur_quest_menu', cur_quest_menu-1),
            ]
        imagebutton align (1580/1920, 340/1080):
            idle '/interface/button/next_idle.webp'
            hover '/interface/button/next_hover.webp'
            insensitive '/interface/button/next_insensitive.webp'
            focus_mask True
            sensitive (cur_quest_menu < number_stages_completed_in_quest[cur_task_menu])
            action [
                SetVariable('cur_quest_menu', cur_quest_menu+1),
            ]

    key 'K_ESCAPE' action Hide('menu_memo')
    key 'mouseup_3' action Hide('menu_memo')

label set_background_nqtr:
    if (not map_open):
        if(isClosedRoom(room_id= cur_room.id, closed_rooms= closed_rooms, now_hour= tm.get_hour_number())):
            # Change the background image to the current room image.
            call closed_room_event
        else:
            $ sp_bg_change_room = getBgRoomRoutine(commitments_in_cur_location, cur_room.id)
            call set_room_background(sp_bg_change_room)
    return

label set_room_background(sp_bg_change_room = ""):
    if (not isNullOrEmpty(sp_bg_change_room)):
        call set_background(sp_bg_change_room)
    else:
        call set_background(cur_room.bg)
    return

# making calls safely:
# Why? Because if I use Call("label") in sleep mode from the room_navigation
# and in the "label" I use "return" an almost all cases the game will end.
label after_return_from_room_navigation(label_name_to_call = ""):
    if isNullOrEmpty(label_name_to_call):
        $ log_error("label_name_to_call is empty", renpy.get_filename_line())
    else:
        $ renpy.call(label_name_to_call)
    call set_background_nqtr
    # Custom Code:
    # ...
    call screen room_navigation
    $ log_error("thera is a anomaly in room_navigation. value: " + label_name_to_call, renpy.get_filename_line())
    jump after_return_from_room_navigation