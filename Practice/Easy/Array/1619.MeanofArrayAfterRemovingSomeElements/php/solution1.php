<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Float
     */
    function trimMean($arr) {
        $N = count($arr);
        $K = intval($N / 20);
        sort($arr);
        $sum = array_sum(array_slice($arr,$K,$N-$K*2));

        return $sum/($N-2*$K);
    }
}