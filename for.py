"""

Домашнее задание №1

Цикл for: Оценки

* создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def count_avg_score(scores: list) -> float:
    return sum(scores)/len(scores)

def main():
    school_classes = [
            {'school_class':'4a','scores':[3,4,4,5,2]},
            {'school_class':'4b','scores':[3,4,4,5,2]},
            {'school_class':'4c','scores':[2,5,5,4,2]},
            {'school_class':'5a','scores':[4,5,4,5,3]},
            {'school_class':'5b','scores':[5,5,5,5,5]},
            ]
    
    classes_avg_scores = []
    for school_class in school_classes:
        class_avg_score = count_avg_score(school_class['scores'])
        classes_avg_scores.append(class_avg_score)
        print(f"В классе {school_class['school_class']} средний балл {class_avg_score}.")
    
    print(f"Средний балл в школе {count_avg_score(classes_avg_scores)}.")

if __name__ == "__main__":
    main()
