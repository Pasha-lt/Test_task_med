# Костышен Павел 093-128-22-25, 9139136@gmail.com
import requests  # pip install requests.


def counter_right_answers(list_answers: list):
    """
    Функция принимает список с ответами(list_answers) отправляет их на сервер,
    а возвращает количество правильных ответов(count).
    :param list_answers - список с ответами.
    :return count - количество правильных ответов.
    """

    count = requests.post(
        'https://tlgrm.info/test/',
        headers={"Content-Type": "application/json"},
        json={"answers": list_answers}
    )

    return count.json()['right_answers']


def start():
    """
    Функция стартует с списка из нулей(list_answers) и каждый индекс(index) от 0 до 24,
    подставляет значением(value) от 0 до 4 пока количество правильных ответов(temporary) не изменится.
    Если количество правильных ответов увеличилось прерываем цикл подстановок, сохранив значение и идем к следующему индексу.
    Если количество правильных ответов уменьшилось прерываем цикл подстановок, и сохраняем то значение которое было изначально.
    :param list_answers - Список с ответами.
    :param index - Значения цикла который мы перебираем и используем как индекс нашего списка.
    :param value - Значения цикла который мы подставляем в значения.
    :param temporary - Временное количество правильных ответов.
    :param counter_right_answers() - Функция принимающая список и возвращающая количество правильных ответов.
    :return list_answers - Список с ответами, но он уже прошел преобразования и является конечным вариантом.
    """
    list_answers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for index in range(25):  # Перебираем индексы.
        temporary = counter_right_answers(list_answers)
        for value in range(4):  # Подставляем значения.
            list_answers[index] = value
            if counter_right_answers(list_answers) > temporary:  # Если количество правильных ответов увеличелось.
                break
            elif counter_right_answers(list_answers) < temporary:  # Если количество правильных ответов уменьшилось.
                list_answers[index] = 0
                break

    return list_answers


if __name__ == '__main__':
    print(f'Правильные ответы - {start()}')

    try:
        assert counter_right_answers(list_answers=[1, 0, 2, 0, 3, 0, 2, 0, 0, 2, 0, 3, 1, 0, 2, 0, 1, 0, 3, 3, 0, 0, 0, 0, 0]) == 8
    except AssertionError:
        print('Тесты отработали некорректно, возможно значение изменены.')
    else:
        print('Тесты отработали корректно.')


