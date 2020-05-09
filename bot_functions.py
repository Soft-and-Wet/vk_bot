import random


class BotFunctions:
    def __init__(self, vk, user_id, event):
        self.user_id = user_id
        self.vk = vk
        self.event = event

    def not_understand(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="Извините, не понимаю, что Вы имели в виду.\n" +
                              "Вы можете воспользоваться командой '/help'",
                              random_id=random.randint(0, 2 ** 64))

    def response_help(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="текст для /help",
                              random_id=random.randint(0, 2 ** 64))
