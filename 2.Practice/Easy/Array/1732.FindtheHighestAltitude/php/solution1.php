<?php

class Solution {

    /**
     * @param Integer[] $gain
     * @return Integer
     */
    function largestAltitude($gain) {
        $curr = 0;
        $max = 0;

        for ($i = 0; $i < count($gain); $i++) {
            $curr += $gain[$i];
            $max = max($max, $curr);
        }

        return $max;
    }
}