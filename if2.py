"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare_strings(string1: str, string2: str) -> int:
    
    if not isinstance(string1,str) or not isinstance(string2,str):
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2):
        return 2
    elif string2 == 'learn':
        return 3
    else:
        return None

def main():

    test_data = [ (1,2),('1',2),(1,'2'),('a','a'),(['a'],'a'),
           ('aa','b'),('ab','learn'),('learn','learn'),('a','bb') ]
    
    for sample in test_data:
        print(compare_strings(*sample))

if __name__ == "__main__":
    main()
