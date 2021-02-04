<?php

class Solution {

    /**
     * @param Integer[] $target
     * @param Integer[] $arr
     * @return Boolean
     */
    function canBeEqual($target, $arr) {
        sort($target);
        sort($arr);

        for($i=0; $i<count($target); $i++) {
            if($target[$i] !== $arr[$i]) {
                return false;
            }
        }

        return true;
    }
}