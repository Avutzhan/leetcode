<?php
//best solution

class BestSolution {

    /**
     * @param Integer[] $candies
     * @param Integer $extraCandies
     * @return Boolean[]
     */
    function kidsWithCandies($candies, $extraCandies) {
        $max = max($candies);
        $ret = array();

        foreach ($candies as $value) {
            $ret[] = $value + $extraCandies >= $max;
        }

        return $ret;
    }
}


//best solution from javascript to php
class Solution {

    /**
     * @param Integer[] $candies
     * @param Integer $extraCandies
     * @return Boolean[]
     */
    function kidsWithCandies($candies, $extraCandies) {
        $ret = [];
        $max = 0;
        for ($i = 0; $i < count($candies); $i++) {
            if ($candies[$i] > $max) {
                $max = $candies[$i];
            }
        }

        for ($i = 0; $i < count($candies); $i++) {
            $ret[] = $candies[$i] + $extraCandies >= $max;
        }

        return $ret;
    }
}