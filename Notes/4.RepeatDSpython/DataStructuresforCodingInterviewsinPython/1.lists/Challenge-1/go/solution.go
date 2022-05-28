package main

import (
  "fmt"
  "reflect"
)

func main() {
  input := []int{1, 2, 3, 5, 6, 7, 8}
  var result []int = remove_even(input)
  expected := []int{1, 3, 5, 7}

  if reflect.DeepEqual(result, expected) {
    fmt.Println("Success")
  } else {
    fmt.Println("Failure")
  }
}

func remove_even(arr []int) []int {
    var res []int

    for _, v := range arr {
        if v % 2 != 0 {
            res = append(res, v)
        }
    }
    return res
}

