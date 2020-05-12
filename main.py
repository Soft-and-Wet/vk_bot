import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from bot_functions import BotFunctions
from bot_conditions import BotConditions
import data


def main_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button("Создать напоминание", color=VkKeyboardColor.POSITIVE)
    keyboard.add_button("Удалить напоминание", color=VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Показать напоминание", color=VkKeyboardColor.DEFAULT)
    keyboard.add_line()
    keyboard.add_button("Играть в города", color=VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()


def reminder_create_keyboard():
    keyboard = VkKeyboard(one_time=False)
    return keyboard.get_empty_keyboard()


def cities_start_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button("Помощь", color=VkKeyboardColor.DEFAULT)
    keyboard.add_button("Завершить игру в города", color=VkKeyboardColor.NEGATIVE)
    return keyboard.get_keyboard()


def main():
    vk_session = vk_api.VkApi(
        token="b368acff9828b8e7933ad148a2973c1ab439fa2b78ad465c0da24f07ec24a4bc105c9f59108874f24e918")
    longpoll = VkBotLongPoll(vk_session, group_id=195170405, wait=10)
    while True:
        for i in data.get_id():
            print(i)
            vk = vk_session.get_api()
            bot_functions = BotFunctions(vk, i, 0)
            # print(type(i[0]))
            if data.reminder_exist(i):
                bot_functions.reminder_reminds(main_keyboard())

        print("_" * 30)

        for event in longpoll.check():

            if event.type == VkBotEventType.MESSAGE_NEW:
                print(event)
                print('Новое сообщение:')
                print('Для меня от:', event.obj.message['from_id'])
                print('Текст:', event.obj.message['text'])

                vk = vk_session.get_api()

                bot_conditions = BotConditions(vk, event.obj.message['from_id'], event)
                bot_functions = BotFunctions(vk, event.obj.message['from_id'], event)

                data.new_user(event.obj.message['from_id'])

                if data.cities_play(event.obj.message['from_id']):
                    if event.obj.message['from_id'] == "Завершить игру в города":
                        bot_conditions.conditions(bot_functions, main_keyboard(), reminder_create_keyboard(),
                                                  cities_start_keyboard())
                    else:
                        bot_functions.cities_play(main_keyboard())
                elif data.reminder_creation(event.obj.message['from_id']):
                    bot_functions.reminder_create_datetime(main_keyboard())
                else:
                    bot_conditions.conditions(bot_functions, main_keyboard(), reminder_create_keyboard(),
                                              cities_start_keyboard())


if __name__ == '__main__':
    main()
