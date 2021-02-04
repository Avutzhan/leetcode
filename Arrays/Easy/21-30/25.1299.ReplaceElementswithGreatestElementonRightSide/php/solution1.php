<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function replaceElements($arr) {
        $prev = -1;
        for ($i = count($arr) - 1; $i >= 0; $i--) {
            $cur = $arr[$i];
            $arr[$i] = $prev;
            $prev = max($prev, $cur);
        }
        return $arr;
    }
}