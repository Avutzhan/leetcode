<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Float
     */
    function findMaxAverage($nums, $k) {
        $sum = 0;

        for ($i = 0; $i < $k; $i++) {
            $sum += $nums[$i];
        }

        $max = $sum;
        for ($i = $k; $i < count($nums); $i++) {
            $sum = $sum - $nums[$i - $k] + $nums[$i];
            $max = max($max, $sum);
        }

        return $max / $k;
    }
}