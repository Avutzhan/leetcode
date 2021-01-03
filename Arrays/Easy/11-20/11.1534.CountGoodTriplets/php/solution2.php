<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function countGoodTriplets($arr, $a, $b, $c) {
        $res = 0;
        $n = count($arr);

        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n - 1; $j++) {
                for ($k = $j + 1; $k < $n; $k++) {
                    if (abs($arr[$i] - $arr[$j]) <= $a && abs($arr[$j] - $arr[$k]) <= $b && abs($arr[$k] - $arr[$i]) <= $c) $res++;
                }
            }
        }

        return $res;
    }
}