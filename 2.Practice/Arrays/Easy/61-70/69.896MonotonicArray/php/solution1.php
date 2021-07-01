<?php

class Solution {

    /**
     * @param Integer[] $A
     * @return Boolean
     */
    function isMonotonic($A) {
        $n = count($A);


        if ($n <= 2) {
            return true;
        }

        $isGreat = false;
        $isLess = false;

        for ($i = 1; $i < $n; $i++) {
            if ($A[$i - 1] > $A[$i]) {
                $isGreat = true;
            }

            if ($A[$i - 1] < $A[$i]) {
                $isLess = true;
            }

            if ($isGreat && $isLess) {
                return false;
            }


        }


        return true;
    }
}