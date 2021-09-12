<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function sortedSquares($nums) {
        $arr = [];
        foreach($nums as $v)
        {
            $arr[] = $v*$v;
        }
        sort($arr);
        return $arr;
    }
}