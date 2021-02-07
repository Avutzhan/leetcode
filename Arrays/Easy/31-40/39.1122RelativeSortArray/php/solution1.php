<?php

class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer[]
     */
    function relativeSortArray($arr1, $arr2) {
        $order = [];
        for ($i = 0; $i < count($arr2); $i++) {
            $order[$arr2[$i]] = $i;
        }

        usort($arr1, function($a, $b) use ($order) {
            if (isset($order[$a]) && isset($order[$b])) {
                return $order[$a] - $order[$b];
            } elseif (isset($order[$a])) {
                return -1;
            } elseif (isset($order[$b])) {
                return 1;
            } else {
                return $a-$b;
            }
        });

        return $arr1;
    }
}