<?php

class Solution {

    /**
     * @param Integer[][] $M
     * @return Integer[][]
     */
    function imageSmoother($M) {
        $result = [];

        for ($i = 0; $i < count($M); $i ++) {
            for ($j = 0; $j < count($M[$i]); $j ++) {
                $result[$i][$j] = $this->_avgSurroundingCells($i, $j, $M);
            }
        }
        return $result;
    }

    private function _avgSurroundingCells($x, $y, $map) {
        list($X, $Y) = [count($map), count($map[0])];
        $sum = $count = 0;

        for ($i = $x - 1; $i <= $x + 1; $i ++) {
            for ($j = $y - 1; $j <= $y + 1; $j ++) {
                if ($i >= 0 && $i < $X && $j >= 0 && $j < $Y) {
                    $sum += $map[$i][$j];
                    $count ++;
                }
            }
        }
        return floor($sum / $count);
    }
}