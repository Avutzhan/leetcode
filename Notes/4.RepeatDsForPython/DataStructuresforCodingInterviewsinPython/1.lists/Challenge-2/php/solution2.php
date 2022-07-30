<?php

function merge(array $arr1, array $arr2): array
{
  $index1 = 0;
  $index2 = 0;

  while ($index1 < count($arr1) && $index2 < count($arr2)) {
    if ($arr1[$index1] > $arr2[$index2]) {
      array_splice($arr1, $index1, 0, $arr2[$index2]);
      $index1++;
      $index2++;
    } else {
      $index1++;
    }
  }

  if ($index2 < count($arr2)) {
    array_push($arr1, ...array_slice($arr2, $index2));
  }

  return $arr1;
}

$result = merge([1, 3, 4, 5],[2, 6, 7, 8]);
$expected = [1, 2, 3, 4, 5, 6, 7, 8];

if (array_diff($result, $expected) == []) {
  echo "Success";
} else {
  echo "failure";
}
