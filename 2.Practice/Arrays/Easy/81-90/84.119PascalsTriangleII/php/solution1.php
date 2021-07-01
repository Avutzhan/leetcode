<?php

class Solution {

    /**
     * @param Integer $rowIndex
     * @return Integer[]
     */
    function getRow($rowIndex) {
        $res = [];

        while (count($res) <= $rowIndex) {
            array_unshift($res, 1);

            for($i = 1; $i < count($res) - 1; $i++) {
                $res[$i] += $res[$i + 1];
            }
        }

        return $res;
    }
}