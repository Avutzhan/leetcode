package main

import "fmt"

func sum(arr []int) int {
  var total int

  for _, v := range arr {
    total += v
  }

  return total
}

func main() {
  items := []int{2,2,2,2,2}
  fmt.Print(sum(items))
}