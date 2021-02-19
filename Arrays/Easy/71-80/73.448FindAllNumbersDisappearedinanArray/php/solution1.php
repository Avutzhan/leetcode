<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findDisappearedNumbers($nums) {
        $result = [];
        $count = count($nums);
        $nums = array_count_values($nums);
        for($i=1; $i<=$count; $i++){
            if(!isset($nums[$i]))   $result[] = $i;
        }

        return $result;
    }
}