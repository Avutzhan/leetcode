<?php

class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @param Integer $d
     * @return Integer
     */
    function findTheDistanceValue($arr1, $arr2, $d) {
        $length1 = count($arr1);
        $length2 = count($arr2);

        $distance = $length1;

        for($i=0; $i<$length1; $i++){
            for($j=0; $j<$length2; $j++){
                if(abs($arr1[$i] - $arr2[$j]) <= $d){
                    $distance -= 1;
                    break;
                }
            }

        }

        return $distance;
    }
}