// https://habr.com/ru/post/456194/

// http://golang-book.ru/chapter-06-arrays-slices-maps.html

// https://coderoad.ru/21326109/%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D1%8E%D1%82%D1%81%D1%8F-%D1%80%D0%B5%D0%B4%D0%BA%D0%BE-%D0%B2-Go

package main

import "fmt"


func main() {
  //array must have one data type values
  //array must have ***FIXED SIZE***

  //init ***ARRAY***
  var array [5]float64

  array[0] = 1
  array[1] = 2
  array[2] = 3
  array[3] = 4
  array[4] = 5
  //array[5] = 6 //size cant be dinamically changed

  var total float64 = 0

  //len returns int data type
  //simple for loop

  // for i := 0; i < len(array); i++ {
  //   total += array[i]
  // }

  //for loop with range
  //you cant create vars that you dont use so this is create an err

  // for i, value := range array {
  //     total += value
  // }

  //change to this
  for _, value := range array {
      total += value
  }

  //short array create method
  // x := [5]float64{ 98, 93, 77, 82, 83 }


  //fmt.Println("\n ARRAY \n")
  //fmt.Print(array, total / float64(len(array)), x) //change data type int to float64(

}