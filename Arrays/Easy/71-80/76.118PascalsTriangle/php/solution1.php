<?php

class Solution {

    /**
     * @param Integer $numRows
     * @return Integer[][]
     */
    function generate($numRows) {
        $pascal = [];

        for ($i = 0; $i < $numRows; $i++) {
            $pascal[$i] = [];
            $pascal[$i][0] = 1;

            for ($j = 1; $j < $i; $j++) {
                $pascal[$i][$j] = $pascal[$i-1][$j-1] + $pascal[$i-1][$j];
            }
            $pascal[$i][$i] = 1;
        }

        return $pascal;
    }
}