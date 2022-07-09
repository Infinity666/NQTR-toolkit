define DEFAULT_LABEL_TALK = "talk"

init -11 python:
    class TalkObject(object):
        """At the inside of the class there are the values used for the talk() function, 
        (all this could be done in Commitment(), but I preferred not to use a dictionary)"""

        def __init__(self,
                    ch_secondary: list[str] = [],
                    bg_before_after: str  = None,
                    after_label_event: str  = None,
                    bg_talk: str  = None,
                    label_talk: str  = None):

            self.ch_secondary = ch_secondary
            self.bg_before_after = bg_before_after
            self.bg_talk = bg_talk
            self.after_label_event = after_label_event
            self.label_talk = label_talk

        def talk(self):
            """Inside you can find the labels and images to start talk()"""
            # if label_talk == None does the default procedure
            if not isNullOrEmpty(self.label_talk):
                renpy.jump(self.label_talk)
            elif not isNullOrEmpty(DEFAULT_LABEL_TALK):
                renpy.jump(DEFAULT_LABEL_TALK)
            return

        def getTalkImage(self):
            """Returns the image during a conversation"""
            return self.bg_talk

        def getBeforeTalkImage(self):
            """Returns the background image used when someone is in the same room. It can be None"""
            return self.bg_before_after

        def getAfterTalkImage(self):
            """Returns the background image used after a conversation, 
            but if after_label_event is not null it passes to after_label_event. 
            ((the latter can be used in case the room is no longer accessible and thus takes you to another room))"""
            if not isNullOrEmpty(self.after_label_event):
                renpy.jump(self.after_label_event)
            else:
                return self.bg_before_after


    def addTalkChoice(ch: str, choice_text: str, label: str, talkch_choices: dict[str, list]): # TODO: add a type for list
        """Add the "choice" in the character's talkch_choices."""
        if (ch in talkch_choices.keys()):
            talkch_choices[ch].append((choice_text, label))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label))
            talkch_choices[ch] = talk_choices
            del talk_choices
        return


    def delTalkChoice(ch: str, choice_text: str, talkch_choices: dict[str, list]): # TODO: add a type for list
        """Deletes the "choice" in the character's talkch_choices."""
        val = 0
        ch_to_del = ch
        for cur_choice in talkch_choices[ch]:
            if cur_choice[0] == choice_text:
                ch_to_del = ch
                break
            else:
                val = val+1
        talkch_choices[ch].pop(val)
        del val
        del ch_to_del
        return
