import random
import data


class BotFunctions:
    def __init__(self, vk, user_id, event):
        self.user_id = user_id
        self.vk = vk
        self.event = event
        self.reminder_creation = False

    def greeting(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="Здравстуйте, " +
                                      self.vk.users.get(user_id=self.event.obj.message['from_id'])[0]['first_name'],
                              random_id=random.randint(0, 2 ** 64))
        self.response_help()

    def not_understand(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="Извините, не понимаю, что Вы имели в виду.\n" +
                                      "Вы можете воспользоваться командой '/help'",
                              random_id=random.randint(0, 2 ** 64))

    def response_help(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="текст для /help\n/reminder",
                              random_id=random.randint(0, 2 ** 64))

    def reminder_create_on(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="введите дату и время напоминания в формате\n'yyyy-mm-dd hh:mm'",
                              random_id=random.randint(0, 2 ** 64))
        data.reminder_creation_change(self.user_id)
        # self.reminder_create_process()

    def reminder_create_process(self):
        dnt = self.event.obj.message['text']
        if len(dnt) == 16:
            if dnt[:3].isdigit() and dnt[5:6].isdigit() and dnt[8:9].isdigit() \
                    and dnt[11:12].isdigit() and dnt[14:15].isdigit():
                # some actions
                self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                                      message="Ваше напоминание <текст> успешно создано",
                                      random_id=random.randint(0, 2 ** 64))
        else:
            self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                                  message="Неверный формат!",
                                  random_id=random.randint(0, 2 ** 64))
        self.reminder_create_off()

    def reminder_create_off(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="Настройка напоминания завершена",
                              random_id=random.randint(0, 2 ** 64))
        data.reminder_creation_change(self.user_id)
