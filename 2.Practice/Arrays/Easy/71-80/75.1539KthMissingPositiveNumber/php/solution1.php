<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function findKthPositive($arr, $k) {
        $i = 0;
        while ($i < count($arr) && $arr[$i] < $i + $k + 1) $i++;
        return $i + $k;
    }
}