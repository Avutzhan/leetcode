function findSmallest($arr) {
  $smallest = $arr[0];
  $smallest_index = 0;

  for ($i = 1; $i < count($arr); $i++) {
    if ($arr[$i] < $smallest) {
      $smallest = $arr[$i];
      $smallest_index = $i;
    }
  }

  return $smallest_index;
}

//из за того что юзаем array_splice нам надо сохранять $len
function selectionSort($arr) {
  $newArr = [];
  for ($i = 0, $len = count($arr); $i < $len; $i++) {
    $smallest = findSmallest($arr);
    $newArr[] = array_splice($arr, $smallest, 1)[0];
  }
  return $newArr;
}

var_dump(selectionSort([5, 3, 6, 2, 10]));