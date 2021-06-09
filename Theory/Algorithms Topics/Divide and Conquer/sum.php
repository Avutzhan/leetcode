<?php

function sum($arr) {
  $total = 0;

  foreach ($arr as $item) {
    $total += $item;
  }

  return $total;
}

var_dump(sum([2,2,2,2,2]));