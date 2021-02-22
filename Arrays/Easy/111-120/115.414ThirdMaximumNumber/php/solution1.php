<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function thirdMax($nums) {
        $first = -INF;
        $second = -INF;
        $third = -INF;

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] === $first || $nums[$i] === $second || $nums[$i] === $third) continue;
            if ($nums[$i] > $first) {
                [$first, $second, $third] = [$nums[$i], $first, $second];
            } else if ($nums[$i] > $second) {
                [$second, $third] = [$nums[$i], $second];
            } else if ($nums[$i] > $third) {
                $third = $nums[$i];
            }
        }

        return $third === -INF ? $first : $third;
    }
}