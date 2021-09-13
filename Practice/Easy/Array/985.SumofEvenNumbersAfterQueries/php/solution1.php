<?php

class Solution {

    /**
     * @param Integer[] $A
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function sumEvenAfterQueries($A, $queries) {
        // result array
        $res = [];

        // current sum of even numbers
        $sum = 0;

        // first, add all even numbers to sum
        for ($i = 0; $i < count($A); $i++) {
            if ($A[$i] % 2 === 0)
                $sum += $A[$i];
        }

        // then, go thru queries
        for ($i = 0; $i < count($queries); $i++) {
            // destructure query
            list($val, $index) = $queries[$i];

            // check if adding val would make it even
            if (($val + $A[$index]) % 2 == 0) {
                // if even, add val, if odd, add new + old
                $A[$index] % 2 == 0
                    ? ($sum += $val)
                    : ($sum += $val + $A[$index]);
            }
            else {
                // if even, subtract old, if odd, do nothing
                $A[$index] % 2 == 0 ? ($sum -= $A[$index]) : false;
            }

            // add val to old
            $A[$index] += $val;

            // push current sum to res
            array_push($res, $sum);

        }

        return $res;
    }
}