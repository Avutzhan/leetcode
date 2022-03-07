<?php

class Solution {

    /**
     * @param String[] $A
     * @return String[]
     */
    function commonChars($A) {
        $cnts = array_fill(0, count($A), array_fill(97, 26, 0));
        for ($i = 0; $i < count($A); $i++)
            for ($j = 0; $j < strlen($A[$i]); $j++)
                $cnts[$i][ord($A[$i][$j])]++;
        $commonCnts = array_fill(97, 26, 0);
        for ($i = 97; $i < 123; $i++) {
            $instances = array_fill(0, count($cnts), 0);
            for ($j = 0; $j < count($cnts); $j++)
                $instances[$j] = $cnts[$j][$i];
            $commonCnts[$i] = min($instances);
        }
        $result = [];
        foreach ($commonCnts as $code => $cnt)
            while ($cnt--) $result[] = chr($code);
        return $result;
    }
}