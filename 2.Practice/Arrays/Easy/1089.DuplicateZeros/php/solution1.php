<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return NULL
     */
    function duplicateZeros(&$arr) {
        for ($i=0; $i<count($arr); $i++) {
            if ($arr[$i] === 0) {
                array_splice($arr, $i, 0, 0);
                array_pop($arr);
                $i+=1;
            }
        }
    }
}