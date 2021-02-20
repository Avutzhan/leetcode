<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function check($nums) {
        $decreased = false;

        for ($i = 1; $i < count($nums); $i += 1) {
            if ($nums[$i] < $nums[$i - 1]) {
                if ($decreased) {
                    return false;
                }
                $decreased = true;
            }
        }

        return $decreased ? $nums[0] >= $nums[count($nums) - 1] : true;
    }
}