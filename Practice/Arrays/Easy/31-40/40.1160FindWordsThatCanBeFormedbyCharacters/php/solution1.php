<?php

class Solution {

    /**
     * @param String[] $words
     * @param String $chars
     * @return Integer
     */
    function countCharacters($words, $chars) {
        $sum = 0;
        $mark = array();
        $mark = array_fill(0, 27, 0);
        $lnth = strlen($chars);
        for($i=0; $i < $lnth; $i++)
            $mark[ord($chars[$i])-96] += 1;
        $lnth = count($words);
        for($i=0; $i<$lnth; $i++)
        {
            $flag = $mark;
            $size = strlen($words[$i]);
            $condition = 1;
            for($j=0; $j<$size; $j++)
            {
                if($flag[ord($words[$i][$j])-96] > 0)
                    $flag[ord($words[$i][$j])-96] -= 1;
                else
                {
                    $condition = 0;
                    break;
                }
            }
            if($condition == 1) $sum += $size;
        }
        return $sum;
    }
}