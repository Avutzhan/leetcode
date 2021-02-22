<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function checkIfExist($A) {
        while (count($A)) { // While the array has items
            $n = array_pop($A); // Get an item and remove it from the array
            // If the double or the half is found stop looking

            if (in_array($n*2, $A) || in_array($n/2, $A)) {
                return true;
            }
        }

        return false; // If we get here we've gone through the whole array without finding a match
    }
}