<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $pieces
     * @return Boolean
     */
    function canFormArray($arr, $pieces) {
        $cache = [];
        $joined = implode('', $arr);

        for ($i = 0; $i < count($pieces); $i++) {
            $piece = $pieces[$i];
            $cache[$piece[0]] = $piece;
        }

        $context = '';
        $idx = 0;

        while ($idx < count($arr)) {
            $value = $arr[$idx];

            $piece = $cache[$value];

            if (!$piece) {
                return false;
            }
            $key = implode('', $piece);

            $context .= $key;

            $idx += count($piece);
        }

        return $context === $joined;
    }
}