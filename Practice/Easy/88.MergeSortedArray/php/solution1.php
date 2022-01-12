<?php

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer $m
     * @param Integer[] $nums2
     * @param Integer $n
     * @return NULL
     */
    function merge(&$nums1, $m, $nums2, $n) {
        $len = $m + $n;
        $m--;
        $n--;
        while ($len--) {
            if ($n < 0 || $nums1[$m] > $nums2[$n]) {
                $nums1[$len] = $nums1[$m--];
            } else {
                $nums1[$len] = $nums2[$n--];
            }
        }
    }
}