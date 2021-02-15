<?php

class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countLargestGroup($n) {
        $m = [];
        $max = 0;

        for ($i = 1; $i <= $n; $i++) {
            $sum = $this->getSum($i);
            if(!isset($m[$sum])) {
                $m[$sum] = 0;
            }
            $m[$sum]++;
            $max = max($max, $m[$sum]);
        }


        return count(array_keys($m, max($m)));
    }

    function getSum($n) {
        $sum = 0;
        while ($n > 0) {
            $sum += $n % 10;
            $n = floor($n / 10);
        }
        return $sum;
    }

}