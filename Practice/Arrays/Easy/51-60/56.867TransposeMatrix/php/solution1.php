<?php

class Solution {

    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    function transpose($A) {
        $res = [];

        for ($i = 0; $i < count($A[0]); $i++) {
            $res[$i] = [];
            for ($j = 0; $j < count($A); $j++) {
                $res[$i][$j] = $A[$j][$i];
            }
        }

        return $res;
    }
}