<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function arrayRankTransform($arr) {
        $hash_map = [];

        $copy_arr = $arr;

        sort($copy_arr);

        $rank = 1;

        for ($i = 0; $i < count($copy_arr); $i++) {

            if ($copy_arr[$i] !== $copy_arr[$i - 1]) {
                $hash_map[$copy_arr[$i]] = $rank;
                $rank += 1;
            }

            var_dump($copy_arr[$i]);
        }

        $re = [];

        foreach ($arr as $i) {
            $re[] = $hash_map[$i];

        }

        return $re;
    }
}