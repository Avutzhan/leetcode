<?php

class Solution {

    /**
     * @param Integer[] $position
     * @return Integer
     */
    function minCostToMoveChips($position) {
        $odd = 0;
        foreach ($position as $p) {
            if ($p %2) $odd++;
        }
        return min(count($position)-$odd, $odd);
    }
}