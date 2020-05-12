class BotConditions:
    def __init__(self, vk, user_id, event):
        self.user_id = user_id
        self.vk = vk
        self.event = event

    def conditions(self, bot_functions, main_keyboard, reminder_create_keyboard,
                   cities_start_keyboard):
        if self.event.obj.message['text'] == "/help":
            pass
            # bot_functions.mini_keyboard(mini_keyboard)
            # bot_functions.response_help(main_keyboard)
        elif self.event.obj.message['text'].lower() == "новое напоминание":
            bot_functions.reminder_create_on(reminder_create_keyboard, main_keyboard)
        elif self.event.obj.message['text'].lower() == "показать напоминание":
            bot_functions.reminder_print(main_keyboard)
        elif self.event.obj.message['text'].lower() == "удалить напоминание":
            bot_functions.reminder_delete(main_keyboard)
        elif self.event.obj.message['text'].lower() == "играть в города":
            bot_functions.cities_start(cities_start_keyboard)
        elif self.event.obj.message['text'].lower() == "завершить":
            bot_functions.cities_end(main_keyboard)
        else:
            bot_functions.not_understand(main_keyboard)
