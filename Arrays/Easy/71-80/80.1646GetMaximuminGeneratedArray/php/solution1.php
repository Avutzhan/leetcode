<?php

class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function getMaximumGenerated($n) {
        $arr = [0, 1];
        $i = 1;
        while ($i++ < $n) $arr[] = $i % 2 == 0 ? $arr[$i / 2] : $arr[($i - 1) / 2] + $arr[($i + 1) / 2];
        return $n < 1 ? 0 : max($arr);
    }
}