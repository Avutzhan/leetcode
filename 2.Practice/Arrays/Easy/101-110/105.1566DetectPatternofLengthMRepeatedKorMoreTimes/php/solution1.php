<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $m
     * @param Integer $k
     * @return Boolean
     */
    function containsPattern($arr, $m, $k) {
        // start with counter = 1
        $count = 1;
        // length of the current window
        $l = 0;
        for ($i = 0; $i < count($arr) - $m; $i += 1) {
            $match = $arr[$i] === $arr[$i + $m];
            if ($match) {
                $l += 1;
                // is pattern found?
                if ($l === $m) {
                    $count += 1;
                    // is no of patterns found?
                    if ($count === $k) {
                        return true;
                    }
                    $l = 0;
                }
            } else {
                // reset counter
                $count = 1;
                $l = 0;
            }
        }
        // did not find the given no of patterns
        return false;
    }
}