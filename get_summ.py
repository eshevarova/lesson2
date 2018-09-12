def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
        print(num_one + num_two)
    except (ValueError, TypeError):
        print('Ты вводишь что-то не то!')


get_summ('15.0', 6)
