<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function specialArray($nums) {
        for ($i = 0; $i <= count($nums); $i++) {
            $c = 0;
            foreach ($nums as $num) {
                $num >= $i && $c++;
            }

            if ($c === $i) {
                return $i;
            }
        }
        return -1;
    }
}