<?php
//best solution simple

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function runningSum($nums) {
        $run = 0;
        $sum = [];

        for($i = 0; $i < count($nums); $i++) {
            $run += $nums[$i];
            $sum[] = $run;
        }

        return $sum;
    }
}