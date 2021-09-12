<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function arrayPairSum($nums) {
        sort($nums);
        $sum = 0;
        for ($i = 0; $i < count($nums); $i += 2) {
            $sum += $nums[$i];
        }
        return $sum;
    }
}