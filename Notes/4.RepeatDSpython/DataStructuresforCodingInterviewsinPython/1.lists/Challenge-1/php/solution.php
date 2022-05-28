<?php

function remove_even(array $array): array
{
  $res = [];
  foreach ($array as $item) {
    if ($item % 2 != 0) {
      $res[] = $item;
    }
  }
  return $res;
}