<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function threeConsecutiveOdds($arr) {
        $count = 0;
        foreach ($arr as $num) {
            if ($num % 2 != 0) {
                $count += 1;
            } else {
                $count = 0;
            }

            if ($count == 3) {
                return true;
            }
        }

        return false;
    }
}