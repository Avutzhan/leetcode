package main

import (
  "fmt"
  "reflect"
)

func main() {
  arr := []int{1, 21, 3, 14, 5, 60, 7, 6}

  var result []int = find_sum(arr, 81)
  expected := []int{21, 60}

  if reflect.DeepEqual(result, expected) {
    fmt.Println("Success")
  } else {
    fmt.Println("Failure")
  }
}

func find_sum(arr []int, k int) []int {
  for i := 0; i < len(arr); i++ {
    for j := 0; j < len(arr); j++ {
      if arr[i] + arr[j] == k && i != j {
        return []int{arr[i], arr[j]}
      }
    }
  }

  return nil
}

