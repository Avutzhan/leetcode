<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxConsecutiveOnes($nums) {
        $count = 0;
        $maxLen = 0;

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === 1) $count++;
            if ($nums[$i + 1] !== 1 && $count > $maxLen) $maxLen = $count;
            if ($nums[$i] === 0) $count = 0;
        }

        return $maxLen;
    }
}