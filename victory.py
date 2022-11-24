import random

# Словарь для перевода даты из формата '01.01.2000' в формат 'первое января 2000 года'
dict_dates = {'27.01.1756': 'двадцать седьмое января 1756 года', '21.03.1685': 'двадцать первое марта 1685 года',
              '04.03.1678': 'четвертое марта 1678 года', '15.06.1843': 'пятнадцатое июня 1843 года',
              '22.10.1811': 'двадцать второе октября 1811 года', '31.01.1797': 'тридцать первое января 1797 года',
              '16.12.1770': 'шестнадцатое декабря 1770 года', '18.08.1750': 'восемнадцатое августа 1750 года',
              '07.05.1840': 'седьмое мая 1840 года', '22.05.1813': 'двадцать второе мая 1813 года'}


# Функция для проверки ответа
def check_answer(answer, correct_answer):
    if answer == correct_answer:
        return 1
    else:
        print('Неверно. Правильная дата рождения:', dict_dates[correct_answer], '\n')
        return 0


# Правильные ответы для каждой знаменитости
Mozart_birthday_year = '27.01.1756'
Bach_birthday_year = '21.03.1685'
Vivaldi_birthday_year = '04.03.1678'
Grieg_birthday_year = '15.06.1843'
Liszt_birthday_year = '22.10.1811'
Schubert_birthday_year = '31.01.1797'
Beethoven_birthday_year = '16.12.1770'
Salieri_birthday_year = '18.08.1750'
Tchaikovsky_birthday_year = '07.05.1840'
Wagner_birthday_year = '22.05.1813'

# Цикл с викториной
while True:
    # Переменная для подсчета количества правильных ответов
    correct_answers = 0

    # Список всех композиторов
    composers = ['Mozart', 'Bach', 'Vivaldi', 'Grieg', 'Liszt',
                 'Schubert', 'Beethoven', 'Salieri', 'Tchaikovsky',
                 'Wagner']

    # Случайно выбираем 5 композиторов из списка для викторины
    result = random.sample(composers, 5)

    # Задаем участнику викторины вопросы, и проверяем ответы
    if 'Mozart' in result:
        Mozart_attempt = input('введите дату рождения Моцарта\n')
        correct_answers += check_answer(Mozart_attempt, Mozart_birthday_year)
    if 'Bach' in result:
        Bach_attempt = input('введите дату рождения Баха\n')
        correct_answers += check_answer(Bach_attempt, Bach_birthday_year)
    if 'Vivaldi' in result:
        Vivaldi_attempt = input('введите дату рождения Вивальди\n')
        correct_answers += check_answer(Vivaldi_attempt, Vivaldi_birthday_year)
    if 'Grieg' in result:
        Grieg_attempt = input('введите дату рождения Грига\n')
        correct_answers += check_answer(Grieg_attempt, Grieg_birthday_year)
    if 'Liszt' in result:
        Liszt_attempt = input('введите дату рождения Листа\n')
        correct_answers += check_answer(Liszt_attempt, Liszt_birthday_year)
    if 'Schubert' in result:
        Schubert_attempt = input('введите дату рождения Шуберта\n')
        correct_answers += check_answer(Schubert_attempt, Schubert_birthday_year)
    if 'Beethoven' in result:
        Beethoven_attempt = input('введите дату рождения Бетховена\n')
        correct_answers += check_answer(Beethoven_attempt, Beethoven_birthday_year)
    if 'Salieri' in result:
        Salieri_attempt = input('введите дату рождения Сальери\n')
        correct_answers += check_answer(Salieri_attempt, Salieri_birthday_year)
    if 'Tchaikovsky' in result:
        Tchaikovsky_attempt = input('введите дату рождения Чайковского\n')
        correct_answers += check_answer(Tchaikovsky_attempt, Tchaikovsky_birthday_year)
    if 'Wagner' in result:
        Wagner_attempt = input('введите дату рождения Вагнера\n')
        correct_answers += check_answer(Wagner_attempt, Wagner_birthday_year)

    # Переменная для неправильных ответов
    incorrect_answers = 5 - correct_answers

    # Выводим в терминал количество правильных ответов
    print('Количество правильных ответов', correct_answers)

    # Выводим в терминал количество неправильных ответов
    print('Количество неправильных ответов', incorrect_answers)

    # Выводим в терминал процент правильных ответов
    print('Процент правильных ответов', correct_answers * 100 / 5)

    # Выводим в терминал процент неправильных ответов
    print('Процент неправильных ответов', incorrect_answers * 100 / 5)

    play_again = input('\nХотите сыграть еще раз?\n')
    if play_again == 'да':
        pass
    else:
        break
