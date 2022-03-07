<?php

class Solution {

    /**
     * @param Integer[][] $nums
     * @param Integer $r
     * @param Integer $c
     * @return Integer[][]
     */
    function matrixReshape($nums, $h, $w) {
        $m = count($nums);
        $n = count($nums[0]);

        if ($m * $n !== $h * $w) {
            return $nums;
        }


        $res = [];
        for ($i = 0, $r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++, $i++) {
                $rr = floor($i / $w);
                if (!$res[$rr]) {
                    array_push($res, []);
                }
                array_push($res[$rr], $nums[$r][$c]);
            }
        }
        return $res;
    }
}