<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findShortestSubArray($nums) {
        $counts = [];
        $firstIndexes = [];
        $lastIndexes = [];
        $max = 0;

        for ($i = 0; $i < count($nums); $i++) {
            $k = $nums[$i];

            if ($counts[$k] != NULL) {
                $counts[$k] = $counts[$k] + 1;
            } else {
                $counts[$k] = 0 + 1;
            }

            $max = max($max, $counts[$k]);

            if ($firstIndexes[$k] === NULL) {
                $firstIndexes[$k] = $i;
            }
            $lastIndexes[$k] = $i;

        }

        $res = count($nums);

        foreach ($counts as $k => $value) {
            if ($counts[$k] === $max) {
                $res = min($res, $lastIndexes[$k] - $firstIndexes[$k] + 1);
            }
        }

        return $res;
    }
}