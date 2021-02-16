<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findLucky($arr) {
        $copy = $arr;
        $counter = [];
        $max = 0;

        //create a map to store frequency counts
        foreach($arr as $num) {
            $count = 0;
            foreach($copy as $item) {
                if ($num == $item) {
                    $count++;
                }
            }

            $counter[$num] = $count;
        }

        //loop through map to find lucky numbers and modify the max value
        foreach ($counter as $key => $value) {
            if ($key == $value) {
                $max = max($max, $value);
            }
        }

        return $max > 0 ? $max : -1;
    }
}