<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function pivotIndex($nums) {
        $sum = $reduce = array_reduce($nums, function($carry, $item) {
            $carry += $item;
            return $carry;
        });

        $sumL = 0;
        for($i=0, $len=count($nums); $i<$len; $i++){
            if ($sumL === ($sum-$nums[$i])/2) {
                return $i;
            }
            $sumL += $nums[$i];
        }
        return -1;
    }
}