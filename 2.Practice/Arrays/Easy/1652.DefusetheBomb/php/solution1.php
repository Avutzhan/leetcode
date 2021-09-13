<?php

class Solution {

    /**
     * @param Integer[] $code
     * @param Integer $k
     * @return Integer[]
     */
    function decrypt($code, $k) {
        $res = array_fill(0, count($code), 0);

        if ($k > 0){
            for ($i = 0; $i < count($code); $i++) {
                $count = 0;
                $j = $i + 1;
                while($count < $k) {
                    if ($j === count($code)) {
                        $j = 0;
                    }
                    $res[$i] += $code[$j];
                    $count = $count + 1;
                    $j++;
                }
            }
        }

        if ($k < 0){
            for($i = 0; $i < count($code); $i++) {
                $count = 0;
                $j = $i - 1;
                while($count > $k) {
                    if ($j === -1) {
                        $j = count($code) - 1;
                    }
                    $res[$i] += $code[$j];
                    $count = $count - 1;
                    $j--;
                }
            }
        }

        return $res;
    }
}