<?php

class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function countNegatives($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $r = $m - 1;
        $c = 0;
        $cnt = 0;

        while ($r >= 0 && $c < $n) {
            if ($grid[$r][$c] < 0) {
                $r--;
                $cnt += $n - $c;
            } else {
                $c++;
            }
        }

        return $cnt;
    }
}