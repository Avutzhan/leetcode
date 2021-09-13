<?php

class Solution {

    /**
     * @param Integer[][] $coordinates
     * @return Boolean
     */
    function checkStraightLine($coords) {
        $n = count($coords);

        for ($i = 0; $i < $n - 2; $i++) {
            $x1 = $coords[$i][0] * $coords[$i + 1][1] + $coords[$i + 1][0] * $coords[$i + 2][1] + $coords[$i + 2][0] * $coords[$i][1];
            $x2 = $coords[$i][1] * $coords[$i + 1][0] + $coords[$i + 1][1] * $coords[$i + 2][0] + $coords[$i + 2][1] * $coords[$i][0];
            $x3 = $x1 - $x2;
            $area = abs(1/2 * $x3);

            if ($area > 0) {
                return false;
            }
        }

        return true;
    }
}