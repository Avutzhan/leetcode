<?php
//best solution simple

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function decompressRLElist($nums) {
        $result = [];

        for ($i = 1; $i < count($nums); $i += 2) {
            for ($j = 0; $j < $nums[$i - 1]; $j++) {
                $result[] = $nums[$i];
            }
        }

        return $result;
    }
}