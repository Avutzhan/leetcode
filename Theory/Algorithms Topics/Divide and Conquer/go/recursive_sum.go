package main

import "fmt"

func sum(arr []int) int {
  if len(arr) == 0 {
    return 0
  }

  return arr[0] + sum(arr[1:])
}

func main() {
  items := []int{1,1,1,1,1}
  fmt.Print(sum(items))
}