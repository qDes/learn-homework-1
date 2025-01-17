"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    answers_dict = {"Как дела?":"Хорошо","Что делаешь?":"Программирую.",
            "Как погода?":"Дождливо."}
    while True:
        try:
            user_question = input("Польователь: ")
            print("Программа:",answers_dict.get(user_question,''))
        except KeyboardInterrupt:
            print("Пока!")
            break

if __name__ == "__main__":
    ask_user()
