## Задача 9. Анализ слова 2
Мы продолжаем писать программы-анализаторы для текста и теперь
от нас требуется реализовать код, с помощью которого можно
будет определять, является ли словом палиндромом - это слово,
которое одинаково читается слева направо и справа налево. 

Напишите такую программу.


#### Пример 1:
```
Введите слово: мадам

Слово является палиндромом
```
#### Пример 2:
```
Введите слово: abccba

Слово является палиндромом
```
#### Пример 3:
```
Введите слово: abbd

Слово не является палиндромом
```

ВАЖНО!
Чтобы корректно отработали автотесты, структура вашей
программы должна быть следующей:

```python
def get_input_parameters():
    """
    Получаем входное слово
    
    :return: например: abccba
    :rtype: str
    """
    # TODO: в этой функции пишем весь необходимый код для 
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(is_palindrome):
    """
    Выводим информацию является ли строка палиндромом
    
    :param is_palindrome: является ли палиндромом, например: True
    :type is_palindrome: bool
    """
    # TODO: в этой функции пишем весь необходимый код 
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def check_palindrome(word):
    """
    Проверяем является ли слово палиндромом.
    
    :param word: слово, например: abccba
    :type word: str
    
    :return: является ли слово палиндром, например: True
    :rtype: bool
    """
    # TODO: в этой функции пишем логику проверки строки на палиндром. 
    #  print'ов и input'ов тут не должно быть. 
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
```