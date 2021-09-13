package main

import "fmt"

func getSmallestIndex(slice[]int) int {
  smallest := slice[0]
  smallest_index := 0

  for i := 1; i < len(slice); i++ {
    if slice[i] < smallest {
      smallest = slice[i]
      smallest_index = i
    }
  }

  return smallest_index

}

func selectSort(datalist[]int) []int {
  var newData []int

  for i, length := 0, len(datalist); i < length; i++ {
    //get index from the smallest value
    smallestIndex := getSmallestIndex(datalist)
    //append the value from the smallest item
    newData = append(newData, datalist[smallestIndex])
    //remove the item just appended
    datalist = append(datalist[:smallestIndex], datalist[smallestIndex+1:]...)

  }

  return newData
}

func RemoveIndex(s []int, index int) []int {
    return append(s[:index], s[index+1:]...)
}

func main() {
  items := []int{5, 3, 6, 2, 10}

  fmt.Println(selectSort(items))
}