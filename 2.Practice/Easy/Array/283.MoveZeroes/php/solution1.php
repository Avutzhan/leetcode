<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    function moveZeroes(&$nums) {
        $pos = 0;

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] !== 0) {
                $nums[$pos++] = $nums[$i];
            }
        }

        for ($i = $pos; $i < count($nums); $i++) {
            $nums[$i] = 0;
        }

    }
}