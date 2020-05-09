class BotConditions:
    def __init__(self, vk, user_id, event):
        self.user_id = user_id
        self.vk = vk
        self.event = event

    def conditions(self, bot_functions):
        if self.event.obj.message['text'] == "/help":
            bot_functions.response_help()
        else:
            bot_functions.not_understand()
