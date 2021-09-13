<?php

class Solution {

    /**
     * @param Integer[] $cost
     * @return Integer
     */
    function minCostClimbingStairs($A) {
        $N = count($A);
        $a = $A[0];
        $b = $A[1];
        $c = -1;
        for ($i = 2; $i < $N; $i++, $a = $b, $b = $c)
            $c = $A[$i] + min($a, $b);
        return min($a, $b);
    }
}