<?php

class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function shiftGrid($grid, $k) {
        $cols = count($grid[0]);
        $rows = count($grid);
        $len = $cols * $rows;
        $items = $this->flatten_array($grid);
        $newGrid = [];

        $step = 0;
        $k = $k % $len;
        while ($step < $k) {
            $end = array_pop($items);
            array_unshift($items, $end);
            $step++;
        }

        for ($i = 0; $i < $rows; $i++) {
            $newGrid[] = [];
            for ($j = 0; $j < $cols; $j++) {
                array_push($newGrid[$i], $items[$i * $cols + $j]);

            }
        }

        return $newGrid;
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