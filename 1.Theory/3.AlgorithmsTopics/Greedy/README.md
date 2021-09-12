
### Greedy

Итак, жадный алгоритм (greedy algorithm) — это алгоритм, который 
на каждом шагу делает локально наилучший выбор в надежде, что 
итоговое решение будет оптимальным.
К примеру, алгоритм Дейкстры нахождения кратчайшего пути в графе 
вполне себе жадный, потому что мы на каждом шагу ищем вершину 
с наименьшим весом, в которой мы еще не бывали, после чего 
обновляем значения других вершин. При этом можно доказать, 
что кратчайшие пути, найденные в вершинах, являются оптимальными.

К слову, алгоритм Флойда, который тоже ищет кратчайшие пути 
в графе (правда, между всеми вершинами), не является примером 
жадного алгоритма. Флойд демонстрирует другой метод — метод 
динамического программирования.

Если глобальная оптимальность алгоритма имеет место практически 
всегда, его обычно предпочитают другим методам оптимизации, таким 
как динамическое программирование.

Использование жадного алгоритма довольно стандартное.
Иногда жадный алгоритм не дает оптимального решения

* Задача составления расписания (жадный алгоритм)
* Задача о рюкзаке (не оптимальный жадный алгоритм)
* Задача о покрытии множества

Идеальное враг хорошего
В некоторых случаях достаточно хорошего ответа (так как идеальный ответ не оптимален и так далее)
такие алгоритмы легко реализовать а полученное решение близко к оптимуму

###Задача о покрытии множества

тут мы должны вычислить под множества. Не существует алгоритма, который будет вычислять подмножества с при­
емле.мой скоростыо! Можно применить только приближенный алгоритм.

Когда вычисление точного решения занимает слишком много времени
применяется приближенный алгоритм. Эффективность приближенного
алгоритма оценивается по 

* быстроте
* близости полученного решения к оптимальному

Вычисление под множеств обычно занимает O(2^n) но если использовать
приближенный алгоритм он ускоряется до O(n^2)

в python мы будем использовать set([]) для множеств

сножества не содержат дубликатов

список станий будет в хэше

###Операции с множествами

фрукты: авокадо помилор банан

Овощи: свекла морковь помидор

* Объединение множеств означает слияние элементов обоих множеств.
* Под операцией пересечения множеств понимается поиск элементов, входящих в оба 
  множества (в данном случае - только помидор).
* Под разностью множеств понимается исключение из одного множества
  элементов, присутствующих в другом множестве.
  
в python

```python
fruits = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])

print(fruits | vegetables) 
# {'avocado', 'beets', 'banana', 'carrots', 'tomato'}
print(fruits & vegetables)
# {'tomato'}
print(fruits - vegetables)
# {'avocado', 'banana'}

```

* множества похожи на списки но множества не содержат дубликатов
* с множествами можно выполнять операции обьединение пересечение разность





