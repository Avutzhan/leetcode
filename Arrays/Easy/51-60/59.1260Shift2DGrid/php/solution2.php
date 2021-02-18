<?php

class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function shiftGrid($grid, $k) {
        $arr = $this->flatten_array($grid);
        while ($k--) {
            $end = array_pop($arr);
            array_unshift($arr, $end);
        }

        $res = [];
        $len = count($grid[0]);
        while (count($arr)) {
            $deleted = array_splice($arr, 0, $len);
            array_push($res, $deleted);
        }

        return $res;
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