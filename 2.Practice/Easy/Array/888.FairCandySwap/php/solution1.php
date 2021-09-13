<?php

class Solution {

    /**
     * @param Integer[] $A
     * @param Integer[] $B
     * @return Integer[]
     */
    function fairCandySwap($A, $B) {
        $suma = array_reduce($A, function($carry, $item) {
            $carry += $item;
            return $carry;
        });

        $sumb = array_reduce($B, function($carry, $item) {
            $carry += $item;
            return $carry;
        });

        $diff = ($suma - $sumb) / 2;

        for ($i=0; $i< count($B); $i++){
            $curr = $B[$i] + $diff;

            if (in_array($curr, $A)) {
                return [$curr, $B[$i]];
            }
        }
    }
}
