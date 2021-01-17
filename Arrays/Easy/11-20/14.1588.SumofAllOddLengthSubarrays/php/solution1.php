<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function sumOddLengthSubarrays($arr) {
        $result = 0;

        for ($i = 0; $i < count($arr); $i++) {
            $currSum = 0;

            for ($j = $i; $j < count($arr); $j++) {
                $currSum += $arr[$j];
                if (($j - $i + 1) % 2 == 1) $result += $currSum;
            }
        }

        return $result;
    }
}