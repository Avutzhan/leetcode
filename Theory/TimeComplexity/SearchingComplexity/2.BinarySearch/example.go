package main

import "fmt"

func binarySearch(datalist[]int, key int) bool {
  low := 0
  high := len(datalist) - 1

  for low <= high {
    mid := (low + high)
    guess := datalist[mid]

    if guess == key {
      return true
    }

    if guess > key {
      high = mid - 1
    } else {
      low = mid + 1
    }

  }

  return false
}

func main() {
  items := []int{1, 3, 5, 7, 9}

  fmt.Println(binarySearch(items, 9))
}