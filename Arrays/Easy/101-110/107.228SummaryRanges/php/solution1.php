<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return String[]
     */
    function summaryRanges($nums) {
        $res = [];

        $left = $nums[0];
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] + 1 !== $nums[$i + 1]) {
                array_push($res, $left === $nums[$i] ? '' . $nums[$i] : $left . '->' . $nums[$i]);

                $left = $nums[$i + 1];
            }
        }
        return $res;
    }
}