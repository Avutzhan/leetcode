<?php

class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Integer[]
     */
    function kWeakestRows($mat, $k) {
        $m = count($mat);

        $n = count($mat[0]);


        $ret = array_fill(0, $k, 0);

        $visited = array_fill(0, $m, 0);
        $idx = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                if ($visited[$j] === 0 && $mat[$j][$i] === 0) {
                    $ret[$idx] = $j;
                    $visited[$j] = 1;
                    $idx++;
                    if ($idx === $k) return $ret;
                }
            }
        }
        for ($i = 0; $i < $m; $i++) {
            if ($visited[$i] === 0) {
                $ret[$idx] = $i;
                $idx++;
                if ($idx === $k) return $ret;
            }
        }
    }
}