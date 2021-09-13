<?php

class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[][] $indices
     * @return Integer
     */
    function oddCells($n, $m, $indices) {
        $rowCount = array_fill(0, $n); // you can omit this and write just [] array
        $columnCount = array_fill(0, $m);
        $ret = 0;

        for ($i = 0; $i < count($indices); $i++) {
            $rowCount[$indices[$i][0]]++;
            $columnCount[$indices[$i][1]]++;
        }

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if (($rowCount[$i] + $columnCount[$j]) % 2 != 0) {
                    $ret++;
                }
            }
        }

        return $ret;
    }
}