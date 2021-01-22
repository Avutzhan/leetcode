<?php
//best solution simple

class Solution {

    /**
     * @param Integer $n
     * @param Integer $start
     * @return Integer
     */
    function xorOperation($n, $start) {
        $result = $start;

        for ($i = 1; $i < $n; $i++) {
            $result = $result ^ ($start + 2 * $i);
        }

        return $result;
    }
}