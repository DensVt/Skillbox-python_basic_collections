def get_input_parameters():
    """
    Получаем входное слово

    :return: входное слово, например: "привет"
    :rtype: str
    """

    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    
    s = input("Введите слово: ")
    return s



def display_result(number_unique_letters):
    """
    Выводим количество уникальных букв в слове

    :param number_unique_letters: количество уникальных букв в слове, например: 6
    :type number_unique_letters: int
    """

    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    
    print('Кол-во уникальных букв: ', number_unique_letters)


def count_number_unique_letters(word):
    """
    Считаем количество уникальных букв в слове.

    :param word: входное слово, например: "привет"
    :type word: str

    :return: количество уникальных букв в слове, например: 6
    :rtype: int
    """

    # TODO: в этой функции пишем логику считаем количество уникальных букв в слове.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    
    return len([i for i in word if word.count(i) == 1])


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
