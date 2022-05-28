package main

import (
  "fmt"
  "reflect"
)

func main() {
  arr1 := []int{1, 3, 4, 5}
  arr2 := []int{2, 6, 7, 8}

  var result []int = merge(arr1, arr2)
  expected := []int{1, 2, 3, 4, 5, 6, 7, 8}

  if reflect.DeepEqual(result, expected) {
    fmt.Println("Success")
  } else {
    fmt.Println("Failure")
  }
}

func merge(arr1 []int, arr2 []int) []int {
    index1 := 0
    index2 := 0
    index_res := 0
    var res []int

    for i := 0; i < len(arr1) + len(arr2); i++ {
        res = append(res, 0)
    }

    for (index1 < len(arr1)) && (index2 < len(arr2)) {
      if arr1[index1] < arr2[index2] {
        res[index_res] = arr1[index1]
        index1 ++
        index_res ++
      } else {
        res[index_res] = arr2[index2]
        index2 ++
        index_res ++
      }
    }

    for index1 < len(arr1) {
      res[index_res] = arr1[index1]
      index1 ++
      index_res ++
    }

    for index2 < len(arr2) {
      res[index_res] = arr2[index2]
      index2 ++
      index_res ++
    }

    return res
}

