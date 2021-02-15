<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minStartValue($nums) {
        $min = 1;
        $sum = 0;

        for($i=0;$i<count($nums);$i++){
            $sum = $sum+$nums[$i];
            $min = min($min,$sum);
        }
        if($min == 1){
            return $min;
        }
        // add 1 to negative of min value obtained to keep the sum always positive
        return (-1*$min)+1;
    }
}
