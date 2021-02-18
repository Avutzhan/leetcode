<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function containsDuplicate($nums) {
        $a = [];

        for ($i = 0; $i < count($nums); $i++) {
            if(isset($a[$nums[$i]])) return true;
            $a[$nums[$i]] = true;
        }

        return false;
    }
}