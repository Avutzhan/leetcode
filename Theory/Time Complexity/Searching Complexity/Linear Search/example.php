<?php

function linearSearch($arr, $x) {
  for ($i = 0; $i < count($arr); $i++) {
    if ($arr[$i] === $x) {
      return $i;
    }
  }

  return -1;
}

$arr = [4, 2, 5, 6, 14, 7, 15, 3];

var_dump(linearSearch($arr, 14));