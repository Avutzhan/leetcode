<?php
//best solution simple

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numIdenticalPairs($nums) {
        $sum = 0;
        for ($i = 0; $i < count($nums); $i++) {
            for ($j = $i + 1; $j < count($nums); $j++) {
                if ($nums[$i] === $nums[$j]) {
                    $sum++;
                }
            }
        }
        return $sum;
    }
}