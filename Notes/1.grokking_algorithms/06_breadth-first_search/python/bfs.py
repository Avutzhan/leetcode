# простая проверка если последняя буква м то это продавец
# можно сделать сложную проверку
from collections import deque


def person_is_seller(name):
    return name[-1] == "m"


# реализуем граф c использованием двусвязного списка
# а в свою очередь двусвязный списко мы реалтзуем в виде массива
graph = {"you": ["alice", "bob", "claire"],
         "bob": ["anuj", "peggy"],
         "alice": ["peggy"],
         "claire": ["thom", "jonny"],
         "anuj": [],
         "peggy": [],
         "thom": [],
         "jonny": []}


# и сама логика поиска в ширину
# получается мы передаем граф функции поиска
# you вернет всех твоих соседей и так далее
def search(name):
    # это новая очередь
    search_queue = deque()
    # создаем очередь  из соседей графа
    search_queue += graph[name]
    # This array is how you keep track of which people you've searched before.
    # а этот массив поможет контролировать повторяющиеся имена
    # он нужен потому что в двусвязном списке может образоваться бесконечный цикл
    # если чел был проверен то он будет тут
    searched = []

    # пока массив не пустой выполняем цикл
    while search_queue:
        # Удаляем элемент из очереди
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        # начинаем поиск только если мы раньше не искали этого человека
        # если нет этого человека в массиве searched выполняем кот
        if not person in searched:
            # выполняем проверку на продавца она должна вернуть true false
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                # если он не продавец то пихаем его обратно в очередь
                search_queue += graph[person]
                # Marks this person as searched
                # и пихаем его в массив searched это означает человек уже проверен
                searched.append(person)
    return False


search("you")
