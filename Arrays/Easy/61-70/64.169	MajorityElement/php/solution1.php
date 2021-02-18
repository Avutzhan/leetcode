<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function majorityElement($nums) {
        sort($nums);
        $cnt = floor(count($nums)) / 2;
        return $nums[$cnt];
    }
}