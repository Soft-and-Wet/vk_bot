class BotConditions:
    def __init__(self, vk, user_id, event):
        self.user_id = user_id
        self.vk = vk
        self.event = event

    def conditions(self, bot_functions):
        if self.event.obj.message['text'] == "/help":
            bot_functions.response_help()
        elif self.event.obj.message['text'] == "/reminder/create":
            bot_functions.reminder_create_on()
        elif self.event.obj.message['text'] == "/reminder/print":
            bot_functions.reminder_print()
        elif self.event.obj.message['text'] == "/reminder/delete":
            bot_functions.reminder_delete()
        elif self.event.obj.message['text'] == "/cities/start":
            bot_functions.cities_start()
        elif self.event.obj.message['text'] == "/cities/end":
            bot_functions.cities_end()
        else:
            bot_functions.not_understand()
