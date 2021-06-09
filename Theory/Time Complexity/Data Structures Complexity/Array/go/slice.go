package main

import "fmt"


func main() {
  //***SLICE***
  var arr2 []int

  arr2 = append(arr2, 1)
  arr2 = append(arr2, 2)
  arr2 = append(arr2, 3)
  arr2 = append(arr2, 4)
  arr2 = append(arr2, 5)

  //make creates slice
  arr3 := make([]int, 5)

  arr3[0] = 1
  arr3[1] = 2
  arr3[2] = 3
  arr3[3] = 4
  arr3[4] = 5
  // arr3[5] = 1 вызовет ошибку так как нет 5 индекса 6 элемент так как мы создавали только 5 но мы можем добавлять и менять размер среза

  arr3 = append(arr3, 6)

  //len cap
  //fmt.Println(arr3)
  //fmt.Println(len(arr3))
  //fmt.Println(cap(arr3))

  //make short slice
  arr4 := make([]int, 5, 6)

  //len cap
  //fmt.Println(arr4)
  //fmt.Println(len(arr4))
  //fmt.Println(cap(arr4))

  arr4[0] = 1
  arr4[1] = 2
  arr4[2] = 3
  arr4[3] = 4
  arr4[4] = 5

  // arr4[5] = 6 вызовет ошибку так как при инициализации мы не добавили этот индекс нужно использовать append чтобы изменить длинну и добавить новый элемент

  arr4 = append(arr4, 6)
  arr4 = append(arr4, 7)
  arr4 = append(arr4, 8)


  // fmt.Println("\n SLICE \n")
  // fmt.Print(arr2, arr3, arr4)

  //Дргуой способ создать срез [low : high]
  //arr[0:] === arr[0:len(arr)]
  //arr[:5] === arr[0:5]
  //arr[:] === arr[0:len(arr)]

  // initarr := [5]int{1,2,3,4,5}

  // sliced := initarr[:5] //same initarr[0:5]
  // chopped := initarr[1:3]

  // append copy
  slice1 := []int{1,2,3}
  // slice2 := append(slice1, 4, 5)

  slice3 := make([]int, 2)
  copy(slice3, slice1)

  fmt.Println(slice1, slice3)


}