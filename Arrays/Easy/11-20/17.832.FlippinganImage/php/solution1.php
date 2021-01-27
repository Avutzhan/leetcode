<?php

class Solution {

    /**
     * @param Integer[][] $A
     * @return Integer[][]
     */
    function flipAndInvertImage($A) {
        for($i = 0; $i < count($A); $i++) {
            $A[$i] = array_reverse($A[$i]);

            for($j = 0; $j < count($A[$i]); $j++) {
                $A[$i][$j] = 1 - $A[$i][$j]; //or A[i][j] ^ 1
            }

        }
        return $A;
    }
}
