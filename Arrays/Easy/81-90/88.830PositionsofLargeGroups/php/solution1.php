<?php

class Solution {

    /**
     * @param String $s
     * @return Integer[][]
     */
    function largeGroupPositions($S) {
        $index = [0, 0];
        $res = [];

        for ($i=0; $i<strlen($S); $i++) {
            if ($i===strlen($S)-1 || $S[$i] !== $S[$i+1]) {
                $index[1] = $i;
                if ($index[1] - $index[0] >= 2) {
                    $res[] = $index;

                }
                $index = [$i+1, $i+1];
            }
        }
        return $res;
    }
}