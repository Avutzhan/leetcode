<?php
//solution 1

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function runningSum($nums) {
        $sum = [];
        for ($i = 0; $i < count($nums); $i++) {
            $sum[$i] = $sum[$i - 1] + $nums[$i];
        }

        return $sum;
    }
}