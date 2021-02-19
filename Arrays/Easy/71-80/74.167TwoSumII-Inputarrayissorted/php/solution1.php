<?php

class Solution {

    /**
     * @param Integer[] $numbers
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($numbers, $target) {
        $l=count($numbers);
        $i=0;
        $j=$l-1;

        while ($numbers[$i]+$numbers[$j] !== $target) {
            if ($numbers[$i]+$numbers[$j] < $target) {
                $i++;
            } else {
                $j--;
            }

        }

        return [$i+1, $j+1];
    }
}