<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function frequencySort($nums) {
        //Collect all number and its frequency
        $counter = $this->count_array($nums);
        //Pre sort
        $pre_sort = $this->pre_sort($counter);
        //Sort
        usort($pre_sort, function($a, $b) {
            return $a[1] == $b[1] ? $b[0] - $a[0] : $a[1] - $b[1];
        });
        //Pre flatten
        $pre_flat = array_map(function($x) {
            $arr = array_fill(0, $x[1], $x[0]);
            return $arr;
        }, $pre_sort);

        return $this->flatten_array($pre_flat);
    }

    function pre_sort(array $array)
    {
        $pre_sort = [];
        foreach($array as $key => $val) {
            $pre_sort[] = [$key, $val];
        }
        return $pre_sort;
    }

    function count_array(array $array)
    {
        $copy = $array;
        $counter = [];

        foreach($array as $num) {
            $count = 0;
            foreach($copy as $item) {
                if ($num == $item) {
                    $count++;
                }
            }

            $counter[$num] = $count;
        }

        return $counter;
    }

    function flatten_array(array $arrays)
    {
        $res = [];
        foreach($arrays as $array) {
            foreach ($array as $item) {
                $res[] = $item;
            }
        }

        return $res;
    }
}