def comparison(first_string, second_string):
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return 0
    elif first_string == second_string:
        return 1
    elif len(first_string) > len(second_string) and second_string != 'learn':
        return 2
    elif second_string == 'learn':
        return 3
    else:
        return 'Введенные строки не соответствуют условиям'


print(comparison('string', 1))
print(comparison('string', 'string'))
print(comparison('string', 'st'))
print(comparison('st', 'string'))
print(comparison('stringgg', 'learn'))
print(comparison('st', 'learn'))
