package main

import "fmt"

func quickSort(arr []int) []int {
  if len(arr) < 2 { //base case return [] and [1]
    return arr
  } else {
    pivot := arr[0]
    var result []int
    var less []int
    var greater []int


    for _, v := range arr[1:] {
      if v <= pivot {
        less = append(less, v)
      }
      if v > pivot {
        greater = append(greater, v)
      }
    }

    result = append(result, quickSort(less)...)
    result = append(result, pivot)
    result = append(result, quickSort(greater)...)

    return result

  }

  return arr
}

func main() {
  items := []int{10, 5, 2, 3}

  fmt.Print(quickSort(items))
}