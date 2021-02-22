<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function searchInsert($nums, $target) {
        foreach($nums as $key => $value)
        {
            if($value >= $target)
            {
                return $key;
                break;
            }
            if(end($nums)<$target)
            {
                return count($nums);
            }
        }
    }
}