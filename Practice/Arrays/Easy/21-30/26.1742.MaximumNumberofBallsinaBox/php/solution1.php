<?php

class Solution {

    /**
     * @param Integer $lowLimit
     * @param Integer $highLimit
     * @return Integer
     */
    function countBalls($lowLimit, $highLimit) {
        $boxes = [];
        $max = 0;
        for($i=$lowLimit;$i<=$highLimit;++$i){
            $s = $this->sumOfDigits($i);
            if(!$boxes[$s]){
                $boxes[$s] = [];
            }
            array_push($boxes[$s], $i);

            $max = max($max, count($boxes[$s]));
        }
        return $max;
    }

    function sumOfDigits($n) {
        $sum = 0;
        while($n>0){
            $sum += $n%10;
            $n = floor($n/10);
        }
        return $sum;
    }
}

