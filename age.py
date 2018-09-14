def pastime(age):
    if age <= 0:
        return 'Вы еще не родились'
    elif age < 7:
        return 'Вы еще ходите в детский сад'
    elif age < 18:
        return 'Вы учитесь в школе'
    elif age < 24:
        return 'Вы учитесь в универе'
    else:
        return 'Вы работаете =('


user_age = int(input('Введите свой возраст:\n'))
result = pastime(user_age)
print(result)
