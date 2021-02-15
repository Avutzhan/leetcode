<?php

class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Boolean
     */
    function isToeplitzMatrix($matrix) {
        for ($i = 0; $i < count($matrix) - 1; $i++) {
            for ($j = 0; $j < count($matrix[0]) - 1; $j++) {
                if ($matrix[$i][$j] != $matrix[$i+1][$j+1]) {
                    return false;
                }
            }
        }

        return true;
    }
}