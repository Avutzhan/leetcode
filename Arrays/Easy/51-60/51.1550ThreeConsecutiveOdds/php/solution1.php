<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function threeConsecutiveOdds($arr) {
        for ($i = 0, $x = 0; $i < count($arr); $i++) {
            $x = $arr[$i] % 2 ? $x | [1, 2, 4][$i % 3] : 0;
            if (7 === $x) return true;
        }
        return false;
    }
}