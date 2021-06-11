<?php

class Solution {

    /**
     * @param Integer[][] $dominoes
     * @return Integer
     */
    function numEquivDominoPairs($dominoes) {
        $map = [];
        $count = 0;

        foreach ($dominoes as $domino) {
            $key = $domino[0] < $domino[1] ? "{$domino[0]}{$domino[1]}" : "{$domino[1]}{$domino[0]}";

            if (array_key_exists($key, $map)) {
                $currentIndex = $map[$key] + 1;
                $map[$key] = $currentIndex;
                $count += $currentIndex;
            } else {
                $map[$key] = 0;
            }
        }

        return $count;
    }
}