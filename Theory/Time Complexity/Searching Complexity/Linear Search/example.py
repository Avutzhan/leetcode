def linearSearch(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i

  return -1

arr = [4, 2, 5, 6, 14, 7, 15, 3]

print(linearSearch(arr, 14)) # 4
