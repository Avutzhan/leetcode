<?php

class Solution {

    /**
     * @param Integer[] $A
     * @param Integer $K
     * @return Integer[]
     */
    function addToArrayForm($A, $K) {
        $flag = count($A) - 1;
        while($K) {
            if($flag < 0) {
                array_unshift($A, $K % 10);
            } else {
                $K += $A[$flag];
                $A[$flag--] = $K % 10;
            }
            $K = floor($K / 10);
        }
        return $A;
    }
}