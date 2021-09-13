<?php

class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $profit = 0;

        for ($i = 1; $i < count($prices); $i++) {
            $prev = $prices[$i - 1];
            $current = $prices[$i];

            if ($prev < $current) {
                $profit += $current - $prev;
            }
        }

        return $profit;
    }
}