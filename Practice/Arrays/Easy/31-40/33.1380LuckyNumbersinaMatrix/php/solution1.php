<?php

class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[]
     */
    function luckyNumbers ($matrix) {
        $m = count($matrix);
        $result = 0;
        $col = 0;

        for ($i = 0; $i < $m; $i++) {
            $minValue = min($matrix[$i]);
            if ($minValue > $result) {
                $result = $minValue;
                $col = $i;
            }
        }

        $maxKey = array_search($result, $matrix[$col]);
        for ($i = 0; $i < $m; $i++) {
            if ($matrix[$i][$maxKey] > $result) {
                return array();
            }
        }
        return array($result);
    }
}