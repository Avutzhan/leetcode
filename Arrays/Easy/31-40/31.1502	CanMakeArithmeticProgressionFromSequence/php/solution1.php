<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canMakeArithmeticProgression($arr) {
        sort($arr);
        for ($i = 2; $i < count($arr); $i++) {
            if ($arr[$i - 1] - $arr[$i - 2] != $arr[$i] - $arr[$i - 1]) {
                return false;

            }
        }
        return true;
    }
}