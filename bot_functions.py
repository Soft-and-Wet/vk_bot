import random
import data
import datetime


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
        self.vk.messages.send(user_id=self.user_id,
                              message="Вот список команд:\n" +
                                      "/reminder/create\n" +
                                      "/reminder/print\n"
                                      "/reminder/delete\n",
                              random_id=random.randint(0, 2 ** 64))

    def reminder_reminds(self):
        print(1)
        dnt, text = data.reminder_print(self.user_id)
        if str(datetime.datetime.today())[:16] == dnt:
            self.reminder_print()
            self.reminder_delete()

    def reminder_create_on(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="Введите дату, время напоминания в формате\n'yyyy-mm-dd hh:mm'\n" +
                                      "В этом же сообщении на следующей строке введите текст напоминания",
                              random_id=random.randint(0, 2 ** 64))
        data.reminder_creation_change(self.user_id)
        # self.reminder_create_process()

    def reminder_create_datetime(self):
        if "\n" in self.event.obj.message['text']:
            dnt, text = self.event.obj.message['text'].split("\n")
            if len(dnt) == 16:
                if dnt[:3].isdigit() and dnt[5:6].isdigit() and dnt[8:9].isdigit() \
                        and dnt[11:12].isdigit() and dnt[14:15].isdigit():
                    data.reminder_datetime_save(self.event.obj.message['from_id'], dnt)
                    data.reminder_text_save(self.event.obj.message['from_id'], text)

                    self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                                          message="Напоминание создано",
                                          random_id=random.randint(0, 2 ** 64))
        else:
            self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                                  message="Неверный формат!",
                                  random_id=random.randint(0, 2 ** 64))
        self.reminder_create_off()
        self.reminder_reminds()

    def reminder_create_off(self):
        self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                              message="Настройка напоминания завершена",
                              random_id=random.randint(0, 2 ** 64))
        data.reminder_creation_change(self.user_id)

    def reminder_print(self):
        if data.reminder_exist(self.user_id):
            dnt, text = data.reminder_print(self.user_id)
            self.vk.messages.send(user_id=self.user_id,
                                  message="Созданное Вами напоминание:\n" +
                                          dnt + "\n" + text,
                                  random_id=random.randint(0, 2 ** 64))
        else:
            self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                                  message="Напоминание не создано",
                                  random_id=random.randint(0, 2 ** 64))

    def reminder_delete(self):
        if data.reminder_exist(self.user_id):
            data.reminder_delete(self.user_id)
            self.vk.messages.send(user_id=self.user_id,
                                  message="Напоминание удалено",
                                  random_id=random.randint(0, 2 ** 64))
        else:
            self.vk.messages.send(user_id=self.event.obj.message['from_id'],
                                  message="Напоминание не создано",
                                  random_id=random.randint(0, 2 ** 64))
