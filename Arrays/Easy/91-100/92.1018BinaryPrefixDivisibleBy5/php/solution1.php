<?php

class Solution {

    /**
     * @param Integer[] $A
     * @return Boolean[]
     */
    function prefixesDivBy5($A) {
        $cur = 0;
        $r = [];

        foreach ($A as $a) {
            var_dump($a);
            $cur = (($cur << 1) | $a) % 5;
            array_push($r, $cur === 0);

        }

        return $r;
    }
}