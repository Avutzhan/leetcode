<?php
//best solution simple

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $index
     * @return Integer[]
     */
    function createTargetArray($nums, $index) {
        $result = [];

        for ($i = 0; $i < count($nums); $i++) {
            array_splice($result, $index[$i], 0, $nums[$i]);
        }

        return $result;
    }
}