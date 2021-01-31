<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProduct($nums) {
        $m1 = 0;
        $m2 = 0;

        for ($i = 0; $i < count($nums); $i++) {
            $m2 = max($m2, min($m1, $nums[$i]));
            $m1 = max($m1, $nums[$i]);
        }
        return ($m1 - 1) * ($m2 - 1);
    }
}