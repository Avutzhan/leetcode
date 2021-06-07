def findSmallest(arr):
  smallest = arr[0] #ля хранения наименьшего значения
  smallest_index = 0 #для хранения его индекса

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i

  return smallest_index

def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
    smallest = findSmallest(arr) #находим наименьший элемент и добавляем в новый массив
    newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))