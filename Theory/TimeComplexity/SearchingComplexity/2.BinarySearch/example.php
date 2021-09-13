<?php

function binarySearch($list, $item) {
    $low = 0;
    $high = count($list) - 1;

    while ($low <= $high) {
        $mid = ($low + $high);
        $guess = $list[$mid];

        if ($guess == $item) {
            return $mid;
        }

        if ($guess > $item) {
            $high = $mid - 1;
        } else {
            $low = $mid + 1;
        }
    }

    return null;
}

$list = [1, 3, 5, 7, 9];
echo binarySearch($list, 9) . "\n";
echo binarySearch($list, -1) . "\n";