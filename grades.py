classes_scores = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                  {'school_class': '6b', 'scores': [5, 5, 5]},
                  {'school_class': '11g', 'scores': [4, 4, 4, 3, 3]}]


def average_scores(school):
    sum_grades = 0
    number_of_grades = 0

    for elem in classes_scores:
        sum_grades += sum(elem['scores'])
        number_of_grades += len(elem['scores'])

    average_school = sum_grades / number_of_grades
    print('Средний балл по школе равен {}'.format(average_school))
    for elem in school:
        print('Средний балл в классе {} равен {}'.format(elem['school_class'],
                                                         (sum(elem['scores']) / len(elem['scores']))))


average_scores(classes_scores)
