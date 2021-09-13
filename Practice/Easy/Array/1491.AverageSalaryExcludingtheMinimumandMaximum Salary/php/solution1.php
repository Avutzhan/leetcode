<?php

class Solution {

    /**
     * @param Integer[] $salary
     * @return Float
     */
    function average($salary) {
        sort($salary);

        // Remove first and last salary
        array_shift($salary);
        array_pop($salary);

        $res = array_reduce($salary, function($carry, $item) {
            $carry += $item;
            return $carry;
        });
        // Get average by summing salaries and dividing by number
        return $res / count($salary);
    }
}