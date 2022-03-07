<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findSpecialInteger($arr) {
        $ws = floor(count($arr) / 4);

        for ($i = 0; $i < count($arr) - $ws; $i++) {
            if ($arr[$i] === $arr[$i + $ws]) {
                return $arr[$i];
            }
        }
        return -1;
    }
}