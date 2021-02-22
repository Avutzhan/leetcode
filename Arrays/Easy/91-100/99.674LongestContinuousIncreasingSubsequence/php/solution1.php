<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findLengthOfLCIS($nums) {
        $len = 1;
        $maxLen = 0;

        for($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] < $nums[$i+1]) {
                $len++;
            } else {
                $len = 1;
            }

            $maxLen = max($len, $maxLen);
        }
        return $maxLen;
    }
}