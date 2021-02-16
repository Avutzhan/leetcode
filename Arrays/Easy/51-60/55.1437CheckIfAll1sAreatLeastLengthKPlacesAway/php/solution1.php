<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        for ($i=-$k-1,  $j=0; $j<count($nums); $j++) {
            if ($nums[$j] == 1) {
                if ($j-$i-1 < $k )
                    return false;
                $i = $j;
            }
        }
        return true;
    }
}
