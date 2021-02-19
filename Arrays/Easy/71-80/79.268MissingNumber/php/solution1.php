<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function missingNumber($nums) {
        $res = array_fill(0, count($nums) + 1,-1);

        foreach ($nums as $num) {
            $res[$num] = $num;
        }
        var_dump($res);
        for ($i = 0; $i < count($res); $i++) {
            if ($res[$i] == -1) {
                return $i;
            }
        }

        return -1;
    }
}