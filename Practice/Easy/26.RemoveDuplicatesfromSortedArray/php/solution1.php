<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        $len = $count = count($nums);
        if ($count < 2) {
            return $count;
        }
        for($i = 1, $j = 0; $i < $count; $i++) {
            if ($nums[$j] == $nums[$i]) {
                unset($nums[$i]);
                $len--;
            }else {
                $j = $i;
            }
        }
    }
}