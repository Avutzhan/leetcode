<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     * Деструктурирующее присваивание доступно в версии 7.1
     * если что моэно отрефакторить быстро
     */
    function maximumProduct($nums) {
        $max1 = -INF;
        $max2 = -INF;
        $max3 = -INF;
        $min2 = INF;
        $min1 = INF;

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] > $max1) {
                [$max1, $max2, $max3] = [$nums[$i], $max1, $max2];
            } else if ($nums[$i] > $max2) {
                [$max2, $max3] = [$nums[$i], $max2];
            } else if ($nums[$i] > $max3) {
                $max3 = $nums[$i];
            }
            if ($nums[$i] < $min1) {
                [$min2, $min1] = [$min1, $nums[$i]];
            } else if ($nums[$i] < $min2) {
                $min2 = $nums[$i];
            }
        }

        return max($max1 * $max2 * $max3, $max1 * $min1 * $min2);
    }
}