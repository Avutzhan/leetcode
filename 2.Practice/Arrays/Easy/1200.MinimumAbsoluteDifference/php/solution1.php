<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[][]
     */
    function minimumAbsDifference($arr) {
        $ans = [];
        sort($arr);
        $minDiff = INF;

        for ($i = 1; $i < count($arr); $i++) {
            $minDiff = min($minDiff, $arr[$i] - $arr[$i - 1]);
        }

        for ($i = 1; $i < count($arr); $i++) {
            if ($arr[$i] - $arr[$i - 1] == $minDiff) {
                $ans[] = [$arr[$i - 1], $arr[$i]];
            }
        }

        return $ans;
    }
}