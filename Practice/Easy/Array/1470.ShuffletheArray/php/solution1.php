<?php
//best solution simple

class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer[]
     */
    function shuffle($nums, $n) {
        $result = [];

        for ($i = 0; $i < $n; $i++) {
            $result[] = $nums[$i];
            $result[] = $nums[$i + $n ];

        }

        return $result;
    }
}

//трассировка алгоритма


class TracingSolution
{

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer[]
     */
    function shuffle($nums, $n)
    {
        var_dump('nums', $nums);
        echo "\n";
        echo "\n";

        var_dump('n', $n);
        echo "\n";
        echo "\n";

        $result = [];

        var_dump('result', $result);
        echo "\n";
        echo "\n";

        for ($i = 0; $i < $n; $i++) {
            $result[] = $nums[$i];
            var_dump('1st', $nums[$i]);
            echo "\n";
            echo "\n";
            $result[] = $nums[$i + $n];
            var_dump('2st', $nums[$i + $n]);
            echo "\n";
            echo "\n";
        }

        return $result;
    }
}

$tsol = new TracingSolution();
var_dump($tsol->shuffle([2, 5, 1, 3, 4, 7], 3));