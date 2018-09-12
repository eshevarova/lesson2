answers_dict = {'Как дела?': 'Прекрасно!', 'Что делаешь?': 'Программирую.', 'На каком языке?': 'Python',
                'Нравится?': 'Ну так', 'Что ты ел сегодня на завтрак?': 'Ты странный..я же не ем..'}


def ask_user():
    while True:
        try:
            answer = input('Что надо?\n')
        except KeyboardInterrupt:
            print('Пока!')
            break
        if answer == 'Прощай':
            break
        if answer in answers_dict.keys():
            print(answers_dict[answer])
        else:
            print('Не понимаю теееееебя')


ask_user()
