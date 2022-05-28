<?php

function merge(array $arr1, array $arr2): array
{
  $index1 = 0;
  $index2 = 0;
  $index_res = 0;
  $res = [];

  for ($i = 0; $i < count($arr1) + count($arr2); $i++) {
    $res[] = 0;
  }

  while ($index1 < count($arr1) && $index2 < count($arr2)) {
    if ($arr1[$index1] < $arr2[$index2]) {
      $res[$index_res] = $arr1[$index1];
      $index1++;
      $index_res++;
    } else {
      $res[$index_res] = $arr2[$index2];
      $index2++;
      $index_res++;
    }
  }

  while ($index1 < count($arr1)){
    $res[$index_res] = $arr1[$index1];
    $index1++;
    $index_res++;
  }

  while ($index2 < count($arr2)) {
    $res[$index_res] = $arr2[$index2];
    $index2++;
    $index_res++;
  }

  return $res;
}

$result = merge([1, 3, 4, 5],[2, 6, 7, 8]);
$expected = [1, 2, 3, 4, 5, 6, 7, 8];

if (array_diff($result, $expected) == []) {
  echo "Success";
} else {
  echo "failure";
}
