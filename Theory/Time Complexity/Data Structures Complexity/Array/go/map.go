package main

import "fmt"

func main() {
  // var x map[string]int
  // x["key"] = 10

  //вызовет ошибку так как нужно инициализировать карту перед использованием

  //init map
  x := make(map[string]int)

  x["key"] = 10
  x["mey"] = 12

  //delete value
  delete(x, "mey")

  //обращение к не существующему ключу вернет 0
  //нулевое значение можно проверить == " "
  //о лучше так
  // name, ok := x["rey"]
  // fmt.Println(name, ok)

  //примерно используется так
  if name, ok := x["rey"]; ok {
    fmt.Print(name)
  } else {
    // fmt.Print("test")
  }

  //сокращенный вариант создания карт
  // y := map[string]int{
  //   "key": 1,
  //   "mey": 2,
  //   "rey": 3,
  // }

  //карты часто ипользуют как многомерный ассоциативный массив
  z := map[string]map[string]int{
    "hi": map[string]int{
      "bob": 18,
      "charly": 22,
    },
    "bye": map[string]int{
      "john": 23,
    },
  }

  if el, ok := z["hi"]; ok {
    fmt.Println(el["bob"])
  }


}