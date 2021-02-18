<?php

class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $rounds
     * @return Integer[]
     */
    function mostVisited($n, $rounds) {
        $start = $rounds[0];
        $end = $rounds[count($rounds)-1];

        $result = [];

        if($start <= $end) {
            for($i = $start; $i <= $end; $i++)  {
                $result[] = $i;
            }

        } else {
            for($i = 1; $i <= $end; $i++) {
                $result[] = $i;
            }

            for($i = $start; $i <= $n; $i++) {
                $result[] = $i;
            }
        }

        return $result;
    }
}