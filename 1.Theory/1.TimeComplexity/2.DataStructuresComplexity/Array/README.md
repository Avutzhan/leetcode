
### Array

|         |Average| Worst |
|:---:    |:---:  |:---:  |
|Access   |   1   |   1   |
|Search   |   n   |   n   |
|Insertion|   n   |   n   |
|Deletion |   n   |   n   |

Space Complexity n

Как работает массив

При использовании массива все задачи хранятся в памяти непрерывно
(рядом друг с другом)

Память заполняется в смешанном виде и если мы успели сохранить 3 задачи
то после этих трех задач возможно сохранятся другие задачи
Но если мы хотим добавить 4 тую задачу то нам придется искать другое
место где могут разместиться уже 4 задачи. Если нужно добавить еще
придется перемещаться еще раз.

Добавление новых элементов в массив это проблема

Можно это обойти бронированием мест

если у вас 3 задачи вы запрашиваете места на 10

у этого решения есть минусы 

* Лишнее место может не понадобиться. И другие не могут его использовать
* Если список будет больше чем резерв то придется опять перемещаться

Связанные списки решают добавление новых элементов

###Плюсы

* Заранее знаете адрес элементов
* Подходят для чтения элементов в произвольных позициях (из-за этого популярны)
* Есть два вида доступа произвольный и последовательный массив поддерживает произвольный
* Многие ситуации требуют произвольного доступа из-за этого массивы популярны
* Массивы и списки нужны для реализации других структур данных 

### Вставка элементов в середину 

Список больше подходит так как просто меняешь адрес предыдущего элемента

А с массивами придется сдвигать вниз все другие элементы а если нет места
все данные будем перемещать в другую область памяти

### Удаление

Список больше подходит так как просто меняешь адрес предыдущего элемента

В массиве при удалении элемента все последующие элементы нужно будет сдвинуть вверх

Массивы на разных языках

### PHP:

* Динамическая типизация. В массив можно добавлять занчения разных типов
* У массивов нет фиксированной длинны
* Если нужна фиксированная длинна используй SplFixedArray но это лишнее

На самом деле массив в PHP - это упорядоченное отображение, которое 
устанавливает соответствие между значением и ключом. Этот тип 
оптимизирован в нескольких направлениях, поэтому вы можете использовать 
его как собственно массив, список (вектор), хеш-таблицу (являющуюся 
реализацией карты), словарь, коллекцию, стек, очередь и, возможно, 
что-то ещё. Так как значением массива может быть другой массив PHP, 
можно также создавать деревья и многомерные массивы.

### JS:

* Динамическая типизация. В массив можно добавлять занчения разных типов
* У массивов нет фиксированной длинны
* Нет Ассоциативного массива его заменяет Обьект что то вроде JSON

### Python3:

Array analog

Стандартная структура данных для хранения нескольких элементов
в определённом порядке в Python называется списком (list), в JavaScript называется массивом (Array).

Associate Array analog

Стандартная структура для хранения данных с возможностью обращения 
по произвольному ключу (отображение) в Python называется dict 
(dictionary, словарь), а в JavaScript — object (объект)

* Динамическая типизация. В массив можно добавлять занчения разных типов
* У массивов нет фиксированной длинны
* Аналог массива Список а аналог ассоциативного массива это Словарь


### Go:             

* Строгая статическая типизация. В массиве только один тип данных.
По идее нельзя изменять размер массива

* Отличие Массива от Среза только одно отсутсвие указания длинны в квадратных скобках

Массив — это нумерованная последовательность элементов одного типа 
с фиксированной длиной

Срез - это часть массива. Как и массивы, срезы индексируются и имеют длину. 
В отличии от массивов их длину можно изменить

[Что такое емкость среза?](https://qna.habr.com/q/356478)

Карта - (также известна как "ассоциативный массив" или "словарь") — это неупорядоченная 
коллекция пар вида ключ-значение

Используй Срезы всегда длина динамически изменяется