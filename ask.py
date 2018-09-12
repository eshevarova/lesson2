answers_dict = {'Хорошо. А у тебя как?': 'Прекрасно!', 'Что делаешь?': 'Программирую.', 'На каком языке?': 'Python',
                'Нравится?': 'Ну так', 'Что ты ел сегодня на завтрак?': 'Ты странный..я же не ем..'}


def ask_user():
    answer = input('Как дела?\n')
    while answer != 'Хорошо':
        if answer in answers_dict.keys():
            print(answers_dict[answer])
        else:
            print('Прости, не понимаю твой вопрос(')
        answer = input()


ask_user()
