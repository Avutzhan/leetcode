<?php

class Solution {

    /**
     * @param Integer[] $A
     * @return Integer[]
     */
    function sortArrayByParityII($A) {
        $result = array_fill(0, count($A), 0);

        for($i = 0, $even = 0, $odd = 1; $i < count($A); $i ++) {
            if($A[$i] % 2 === 0) {
                $result[$even] = $A[$i];
                $even += 2;
            } else {
                $result[$odd] = $A[$i];
                $odd += 2;
            }
        }
        return $result;
    }
}