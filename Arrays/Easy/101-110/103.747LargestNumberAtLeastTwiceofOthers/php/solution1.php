<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function dominantIndex($nums) {
        $first = -INF;
        $second = -INF;
        $ans = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] > $first) {
                $second = $first;
                $first = $nums[$i];
                $ans = $i;
            } else if ($nums[$i] > $second) {
                $second = $nums[$i];
            }
        }
        return $first >= $second * 2 ? $ans : -1;
    }
}