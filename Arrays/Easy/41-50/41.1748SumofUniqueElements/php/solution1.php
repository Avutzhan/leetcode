<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfUnique($nums) {
        $sum =0;
        $a = $nums;
        foreach ($a as $t) {
            $count =0;

            for ($q =0;$q<count($nums);$q++){
                if($nums[$q]==$t) $count++;
            }

            if($count<=1) $sum+=$t;
        }
        return $sum;
    }
}