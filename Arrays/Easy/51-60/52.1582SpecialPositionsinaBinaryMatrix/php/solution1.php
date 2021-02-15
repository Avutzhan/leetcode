<?php

class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function numSpecial($mat) {
        $M = count($mat);
        $N = count($mat[0]);
        $cnt = 0;
        $row = array_fill(0, $M, 0);
        $col = array_fill(0, $N, 0);
        for ($i = 0; $i < $M; $i++) {
            for ($j = 0; $j < $N; $j++) {
                if ($mat[$i][$j]) {
                    $row[$i]++;
                    $col[$j]++;
                }

            }

        }

        for ($i = 0; $i < $M; $i++) {
            for ($j = 0; $j < $N; $j++) {
                if ($mat[$i][$j] && $row[$i] == 1 && $col[$j] == 1) {
                    $cnt++;
                }
            }

        }

        return $cnt;
    }
}