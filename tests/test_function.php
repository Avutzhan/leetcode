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

$result = remove_even([-66, -169, 62, 199, 19, 112, -49, -131, -177, -141, -120, 174, 164, 33, 167, -127, 93, 76, 163, -117, 60, 183, -118, -135, -43, 68, -111, -47, 6, -185, 50, -34, -73, 72, 90, 74, 48, -112, -198, -51, 77, -81, 9, 21, 198, 40, -105, 116, 158, -115, -119, -97, 73, 86, 187, 143, 24, -36, 120, 101, 105, 117, 91, 194, -92, 180, 123, -173, -193, -57, 188, -55, -28, -9, 127, -99, 169, -82, -192, 176, -42, -72, 126, -187, 121, -6, -3, 41]);
$expected = [-169, 199, 19, -49, -131, -177, -141, 33, 167, -127, 93, 163, -117, 183, -135, -43, -111, -47, -185, -73, -51, 77, -81, 9, 21, -105, -115, -119, -97, 73, 187, 143, 101, 105, 117, 91, 123, -173, -193, -57, -55, -9, 127, -99, 169, -187, 121, -3, 41];

if (array_diff($result, $expected) == []) {
  echo "Success";
} else {
  echo "failure";
}
