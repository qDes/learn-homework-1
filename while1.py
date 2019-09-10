"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    user_phrase = ''
    while user_phrase != "Хорошо":
        print('Как дела?')
        user_phrase = input()

    
if __name__ == "__main__":
    ask_user()
