import sqlite3
from random import choice

con = sqlite3.connect("data.db")
cur = con.cursor()

cities = ['Абакан', 'Азов', 'Александров', 'Алексин', 'Альметьевск', 'Анапа', 'Ангарск', 'Анжеро-Судженск', 'Апатиты',
          'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск', 'Асбест', 'Астрахань', 'Ачинск', 'Балаково',
          'Балахна', 'Балашиха', 'Балашов', 'Барнаул', 'Батайск', 'Белгород', 'Белебей', 'Белово', 'Белогорск',
          'Белорецк', 'Белореченск', 'Бердск', 'Березники', 'Березовский', 'Бийск', 'Биробиджан', 'Благовещенск',
          'Бор', 'Борисоглебск', 'Боровичи', 'Братск', 'Брянск', 'Бугульма', 'Буденновск', 'Бузулук', 'Буйнакск',
          'Великие Луки', 'Великий Новгород', 'Верхняя Пышма', 'Видное', 'Владивосток', 'Владикавказ', 'Владимир',
          'Волгоград', 'Волгодонск', 'Волжск', 'Волжский', 'Вологда', 'Вольск', 'Воркута', 'Воронеж', 'Воскресенск',
          'Воткинск', 'Всеволожск', 'Выборг', 'Выкса', 'Вязьма', 'Гатчина', 'Геленджик', 'Георгиевск', 'Глазов',
          'Горно-Алтайск', 'Грозный', 'Губкин', 'Гудермес', 'Гуково', 'Гусь-Хрустальный', 'Дербент', 'Дзержинск',
          'Димитровград', 'Дмитров', 'Долгопрудный', 'Домодедово', 'Донской', 'Дубна', 'Евпатория', 'Егорьевск',
          'Ейск', 'Екатеринбург', 'Елабуга', 'Елец', 'Ессентуки', 'Железногорск', 'Железногорск', 'Жигулевск',
          'Жуковский', 'Заречный', 'Зеленогорск', 'Зеленодольск', 'Златоуст', 'Иваново', 'Ивантеевка', 'Ижевск',
          'Избербаш', 'Иркутск', 'Искитим', 'Ишим', 'Ишимбай', 'Йошкар-Ола', 'Казань', 'Калининград', 'Калуга',
          'Каменск-Уральский', 'Каменск-Шахтинский', 'Камышин', 'Канск', 'Каспийск', 'Кемерово', 'Керчь', 'Кинешма',
          'Кириши', 'Киров', 'Кирово-Чепецк', 'Киселевск', 'Кисловодск', 'Клин', 'Клинцы', 'Ковров', 'Когалым',
          'Коломна', 'Комсомольск-на-Амуре', 'Копейск', 'Королев', 'Кострома', 'Котлас', 'Красногорск', 'Краснодар',
          'Краснокаменск', 'Краснокамск', 'Краснотурьинск', 'Красноярск', 'Кропоткин', 'Крымск', 'Кстово', 'Кузнецк',
          'Кумертау', 'Кунгур', 'Курган', 'Курск', 'Кызыл', 'Лабинск', 'Лениногорск', 'Ленинск-Кузнецкий',
          'Лесосибирск', 'Липецк', 'Лиски', 'Лобня', 'Лысьва', 'Лыткарино', 'Люберцы', 'Магадан', 'Магнитогорск',
          'Майкоп', 'Махачкала', 'Междуреченск', 'Мелеуз', 'Миасс', 'Минеральные Воды', 'Минусинск', 'Михайловка',
          'Михайловск', 'Мичуринск', 'Москва', 'Мурманск', 'Муром', 'Мытищи', 'Набережные Челны', 'Назарово',
          'Назрань', 'Нальчик', 'Наро-Фоминск', 'Находка', 'Невинномысск', 'Нерюнгри', 'Нефтекамск', 'Нефтеюганск',
          'Нижневартовск', 'Нижнекамск', 'Нижний Новгород', 'Нижний Тагил', 'Новоалтайск', 'Новокузнецк',
          'Новокуйбышевск', 'Новомосковск', 'Новороссийск', 'Новосибирск', 'Новотроицк', 'Новоуральск',
          'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый Уренгой', 'Ногинск', 'Норильск', 'Ноябрьск',
          'Нягань', 'Обнинск', 'Одинцово', 'Озерск', 'Октябрьский', 'Омск', 'Орел', 'Оренбург', 'Орехово-Зуево',
          'Орск', 'Павлово', 'Павловский Посад', 'Пенза', 'Первоуральск', 'Пермь', 'Петрозаводск',
          'Петропавловск-Камчатский', 'Подольск', 'Полевской', 'Прокопьевск', 'Прохладный', 'Псков', 'Пушкино',
          'Пятигорск', 'Раменское', 'Ревда', 'Реутов', 'Ржев', 'Рославль', 'Россошь', 'Ростов-на-Дону', 'Рубцовск',
          'Рыбинск', 'Рязань', 'Салават', 'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов',
          'Саров', 'Свободный', 'Севастополь', 'Северодвинск', 'Северск', 'Сергиев Посад', 'Серов', 'Серпухов',
          'Сертолово', 'Сибай', 'Симферополь', 'Славянск-на-Кубани', 'Смоленск', 'Соликамск', 'Солнечногорск',
          'Сосновый Бор', 'Сочи', 'Ставрополь', 'Старый Оскол', 'Стерлитамак', 'Ступино', 'Сургут', 'Сызрань',
          'Сыктывкар', 'Таганрог', 'Тамбов', 'Тверь', 'Тимашевск', 'Тихвин', 'Тихорецк', 'Тобольск', 'Тольятти',
          'Томск', 'Троицк', 'Туапсе', 'Туймазы', 'Тула', 'Тюмень', 'Узловая', 'Улан-Удэ', 'Ульяновск', 'Урус-Мартан',
          'Усолье-Сибирское', 'Уссурийск', 'Усть-Илимск', 'Уфа', 'Ухта', 'Феодосия', 'Фрязино', 'Хабаровск',
          'Ханты-Мансийск', 'Хасавюрт', 'Химки', 'Чайковский', 'Чапаевск', 'Чебоксары', 'Челябинск', 'Черемхово',
          'Череповец', 'Черкесск', 'Черногорск', 'Чехов', 'Чистополь', 'Чита', 'Шадринск', 'Шали', 'Шахты', 'Шуя',
          'Щекино', 'Щелково', 'Электросталь', 'Элиста', 'Энгельс', 'Южно-Сахалинск', 'Юрга', 'Якутск', 'Ялта',
          'Ярославль']


def new_user(user_id, event):
    if not cur.execute("""SELECT id FROM Table1 WHERE id = ?""", (user_id,)).fetchall():
        print("---------------------------------")
        cur.execute(f"INSERT INTO Table1(id) VALUES({user_id})")
        cur.execute("""INSERT INTO Table1(reminder_creation) VALUES(0)""")
        cur.execute("""INSERT INTO Table1(cities_play) VALUES(0)""")
        cur.execute("""INSERT INTO Table1(cities) VALUES()""")
        # cur.execute("""INSERT INTO Table1(reminder_datetime) VALUES("")""")
        # cur.execute(f"INSERT INTO Table1(event) VALUES({event})")
        con.commit()


def reminder_creation(user_id):
    if cur.execute("""SELECT reminder_creation FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] == 1:
        return True
    else:
        return False


def get_id():
    return cur.execute("""SELECT id FROM Table1""").fetchall()[1:]


def reminder_reminds(vk_session):
    print(0)
    for user_id in cur.execute("""SELECT id FROM Table1""").fetchall():
        print(user_id[0])
    # vk = vk_session.get_api()
    # bot_functions = BotFunctions(vk, event.obj.message['from_id'], event)
    # if reminder_exist(event.obj.message['from_id']):
    # bot_functions.reminder_reminds()
    # if reminder_exist(user_id[0]):


def reminder_creation_change(user_id):
    if cur.execute("""SELECT reminder_creation FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] == 1:
        cur.execute("""UPDATE Table1 SET reminder_creation = 0 WHERE id = ?""", (user_id,))
    else:
        cur.execute("""UPDATE Table1 SET reminder_creation = 1 WHERE id = ?""", (user_id,))
    con.commit()
    # print(cur.execute("""SELECT reminder_creation FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0])


def reminder_datetime_save(user_id, datetime):
    cur.execute("""UPDATE Table1 SET reminder_datetime = ? WHERE id = ?""", (datetime, user_id,))
    con.commit()


def reminder_text_save(user_id, text):
    cur.execute("""UPDATE Table1 SET reminder_text = ? WHERE id = ?""", (text, user_id,))
    con.commit()


def reminder_delete(user_id):
    cur.execute("""UPDATE Table1 SET reminder_datetime = ? WHERE id = ?""", (None, user_id,))
    cur.execute("""UPDATE Table1 SET reminder_text = ? WHERE id = ?""", (None, user_id,))
    con.commit()


def reminder_print(user_id):
    return cur.execute("""SELECT reminder_datetime FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0], \
           cur.execute("""SELECT reminder_text FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0]


def reminder_exist(user_id):
    # print(cur.execute("""SELECT reminder_datetime FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0])
    if user_id is not None:
        if cur.execute("""SELECT reminder_datetime FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] is not None:
            return True
        else:
            return False


def cities_play_change(user_id):
    if cur.execute("""SELECT cities_play FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] == 1:
        cur.execute("""UPDATE Table1 SET cities_play = 0 WHERE id = ?""", (user_id,))
    else:
        cur.execute("""UPDATE Table1 SET cities_play = 1 WHERE id = ?""", (user_id,))
    con.commit()


def cities_play(user_id):
    if cur.execute("""SELECT cities_play FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] == 1:
        return True
    else:
        return False


def cities_play_end(user_id):
    cur.execute("""UPDATE Table1 SET cities = "" WHERE id = ?""", (user_id,))
    con.commit()


# cities_play_end(415484733)


def cities_play_add(user_id, city):
    cur.execute("""UPDATE Table1 SET cities = ? WHERE id = ?""", (
        cur.execute("""SELECT cities FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] + city, user_id,))
    con.commit()


def cities_play_isrepeat(user_id, city):
    print(cur.execute("""SELECT cities FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0])
    print(city)
    if cur.execute("""SELECT cities FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0] == "":
        cities_play_add(user_id, city)
        return True
    elif city[0].lower() == cur.execute("""SELECT cities FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0][-1]:
        if city not in cur.execute("""SELECT cities FROM Table1 WHERE id = ?""", (user_id,)).fetchall()[0][0]:
            cities_play_add(user_id, city)
            return True
        else:
            return False
    else:
        return False


def cities_play_new(user_id, city):
    while True:
        new_city = choice(cities)
        if new_city[0].lower() == city[-1] \
                and new_city not in cur.execute("""SELECT cities FROM Table1 WHERE id = ?""", (user_id,)).fetchall():
            cities_play_add(user_id, new_city)
            return new_city
