#В переменных low и high хранятся границы той части списка в которой выполняется поиск
def binarySearch(list, item):
  low = 0 #start
  high = len(list)-1 #end

  while low <= high: #пока эта часть не сократится до одного элемента
    mid = (low + high) #проверяем средний элемент
    guess = list[mid]
    if guess == item: #значение найдено
      return mid
    #если значение под этим индексов больше искомого значения
    #то сдвигаем конец на середину если меньше то сдвигаем начало на середину
    if guess > item: #много
      high = mid - 1
    else:            #мало
      low = mid + 1

  return None        #значение не существует

myList = [1, 3, 5, 7, 9]

print(binarySearch(myList, 9))