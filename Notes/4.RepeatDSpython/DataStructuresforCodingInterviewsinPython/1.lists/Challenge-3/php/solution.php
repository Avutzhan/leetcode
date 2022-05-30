<?php

function find_sum(array $arr, int $k): array
{
  for ($i = 0; $i < count($arr); $i++) {
    for ($j = 0; $j < count($arr); $j++) {
      if ($arr[$i] + $arr[$j] == $k && $i != $j) {
        return [$arr[$i], $arr[$j]];
      }
    }
  }
}

$result = find_sum([1, 21, 3, 14, 5, 60, 7, 6],81);
$expected = [21, 60];

if (array_diff($result, $expected) == []) {
  echo "Success";
} else {
  echo "failure";
}
