<?php

class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function diagonalSum($mat) {
        $n = count($mat);

        $m = floor($n / 2);

        $res = 0;

        for ($i = 0; $i < $n; $i++) {
            $res += $mat[$i][$i];
            $res += $mat[$n - 1 - $i][$i];
        }

        if ($n % 2 == 1) {
            $res -= $mat[$m][$m];
        }

        return $res;
    }
}