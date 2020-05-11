import sys

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot_functions import BotFunctions
from bot_conditions import BotConditions
import data
import threading
import subprocess


def main():
    vk_session = vk_api.VkApi(
        token="b368acff9828b8e7933ad148a2973c1ab439fa2b78ad465c0da24f07ec24a4bc105c9f59108874f24e918")
    longpoll = VkBotLongPoll(vk_session, group_id=195170405, wait=10)
    while True:
        for i in data.get_id():
            print(i[0])
            vk = vk_session.get_api()
            bot_functions = BotFunctions(vk, i[0], 0)
            print(type(i[0]))
            if data.reminder_exist(i[0]):
                bot_functions.reminder_reminds()

        for event in longpoll.check():
            data.reminder_reminds(vk_session)
            if event.type == VkBotEventType.MESSAGE_NEW:
                print(event)
                print('Новое сообщение:')
                print('Для меня от:', event.obj.message['from_id'])
                print('Текст:', event.obj.message['text'])

                vk = vk_session.get_api()

                response = vk.users.get(user_id=event.obj.message['from_id'])
                # print(response[0])

                bot_functions = BotFunctions(vk, event.obj.message['from_id'], event)
                bot_conditions = BotConditions(vk, event.obj.message['from_id'], event)

                data.new_user(event.obj.message['from_id'], event)

                # print(bot_functions.reminder_creation)

                if data.reminder_exist(event.obj.message['from_id']):
                    bot_functions.reminder_reminds()

                if not data.reminder_creation(event.obj.message['from_id']):
                    bot_conditions.conditions(bot_functions)
                else:
                    bot_functions.reminder_create_datetime()


if __name__ == '__main__':
    main()
