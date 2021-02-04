<?php

class Solution {

    /**
     * @param Integer[] $A
     * @return Integer[]
     */
    function sortArrayByParity($A) {
        $B = [];
        foreach ($A as $a) {
            if ($a % 2 === 1) {
                array_push($B, $a);
            } else {
                array_unshift($B, $a);
            }
        }

        return $B;
    }
}