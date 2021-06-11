<?php

class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $min = INF; //max save integer 9007199254740991 or write just INF
        $max = 0;
        for ($i = 0; $i < count($prices); $i++) {
            $min = min($min, $prices[$i]);
            $max = max($max, $prices[$i] - $min);
        }
        return $max;
    }
}