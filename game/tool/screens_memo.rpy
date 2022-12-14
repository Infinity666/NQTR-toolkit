# Id of the task selected in the menu
default cur_task_menu = ""
# quest level based on the task selected in the menu
default cur_quest_menu = ""

default gui.menu_memo_image_ysize = 400
default gui.menu_memo_image_xsize = 800
default gui.menu_memo_frame_xsize = 1190
default gui.menu_memo_frame_ysize = 400
default gui.menu_memo_frame_xalign = 0.72
default gui.menu_memo_frame_yalign = 0.6

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
        ysize gui.lateralframescroll_ysize
        background None
        # task title list
        viewport mousewheel True draggable True id 'vp1':
            has vbox spacing 5
            for task_id in current_quest_stages.keys():
                button:
                    xpos gui.interface_text_size
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
            xalign gui.menu_memo_frame_xalign
            yalign gui.menu_memo_frame_yalign
            # Image
            if quest_menu.bg != '' and quest_menu.bg != None:
                add Frame(quest_menu.bg, Borders(0,0,0,0)):
                    xsize gui.menu_memo_image_xsize
                    ysize gui.menu_memo_image_ysize
                    xalign 0.5
                    yalign 0
            elif quests[cur_task_menu].bg != '' and quests[cur_task_menu].bg != None:
                add Frame(quests[cur_task_menu].bg, Borders(0,0,0,0)):
                    xsize gui.menu_memo_image_xsize
                    ysize gui.menu_memo_image_ysize
                    xalign 0.5
                    yalign 0

            text quest_menu.title:
                size gui.interface_text_size
                xalign 0.5

            frame:
                # area (0, 0, 1190, 400)
                xsize gui.menu_memo_frame_xsize
                ysize gui.menu_memo_frame_ysize
                background None

                has hbox
                viewport mousewheel True draggable True id 'vp2':
                    has vbox spacing 30
                    if cur_task_menu in quests_descriptions:
                        text quests_descriptions[cur_task_menu] size gui.normal_text_size color gui.accent_color
                    else:
                        text quests[cur_task_menu].description size gui.normal_text_size color gui.accent_color
                    if (current_quest_stages[cur_task_menu].active):
                        text quest_menu.description size gui.normal_text_size
                        text quest_menu.advice size gui.big_normal_text_size
                        for item in quest_menu.goals:
                            text item.description size gui.big_normal_text_size
                        if current_quest_stages[cur_task_menu].completed and (cur_quest_menu+1) == len(quests[cur_task_menu].stages_id):
                            if quests[cur_task_menu].development:
                                text _("It is currently the end of this story, unfortunately you have to wait for an update to continue this story.") size gui.big_normal_text_size
                            else:
                                text _("You have completed all the quests.") size gui.big_normal_text_size
                    else:
                        text quest_menu.request_description size gui.normal_text_size color gui.accent_color
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
