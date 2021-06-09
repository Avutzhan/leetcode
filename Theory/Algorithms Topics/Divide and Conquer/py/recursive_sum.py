##recursive

def sum(arr):
  if arr == []:
    return 0

  return arr[0] + sum(arr[1:])

print(sum([2,2,2,2,2]))