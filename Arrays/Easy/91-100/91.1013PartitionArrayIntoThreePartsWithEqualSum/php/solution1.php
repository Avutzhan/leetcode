<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canThreePartsEqualSum($A) {
        $reduce = array_reduce($A, function($carry, $item) {
            $carry += $item;
            return $carry;
        });
        $sum = $reduce / 3;
        $s = 0;
        $count = 0;

        for($i=0;$i<count($A);$i++){
            $s+=$A[$i];
            if ($s===$sum) {
                $count++;
                $s=0;
            }
        }
        return $count>=3;
    }
}