user_age = int(input('Введите свой возраст:\n'))


def pastime(age):
    if age < 7:
        return 'Вы еще ходите в детский сад'
    elif 7 <= age < 18:
        return 'Вы учитесь в школе'
    elif 18 <= age < 24:
        return 'Вы учитесь в универе'
    elif age >= 24:
        return 'Вы работаете =('

result = pastime(user_age)
print(result)
