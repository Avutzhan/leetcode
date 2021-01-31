<?php

class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function sumZero($n) {
        $arr = array_fill(0, $n);

        for ($i = 0; $i < $n; $i++) {
            $arr[$i] = $i * 2 - $n + 1;
        }

        return $arr;
    }
}