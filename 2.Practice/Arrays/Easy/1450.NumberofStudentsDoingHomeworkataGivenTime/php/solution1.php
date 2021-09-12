<?php

class Solution {

    /**
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @param Integer $queryTime
     * @return Integer
     */
    function busyStudent($startTime, $endTime, $queryTime) {
        $res = 0;

        for ($i = 0; $i < count($startTime); $i++) {
            if ($startTime[$i] <= $queryTime && $queryTime <= $endTime[$i] ) {
                $res++;
            }
        }

        return $res;
    }
}