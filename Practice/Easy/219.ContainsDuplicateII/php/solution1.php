<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function containsNearbyDuplicate($nums, $k) {
        $ind = [];
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if (array_key_exists($nums[$i], $ind) && $i - $ind[$nums[$i]] <= $k) {
                return true;
            }
            $ind[$nums[$i]] = $i;
        }
        return false;
    }
}