<?php

class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function minTimeToVisitAllPoints($points) {
        $ans = 0;

        for ($i = 1; $i < count($points); $i++) {
            $current = $points[$i];
            $prev = $points[$i - 1];

            $ans += max(abs($current[0] - $prev[0]), abs($current[1] - $prev[1]));
        }

        return $ans;
    }
}