<?php

class Solution {

    /**
     * @param Integer[] $deck
     * @return Boolean
     */
    function hasGroupsSizeX($deck) {
        $buckets = [];

        foreach($deck as $card) {
            $count = $buckets[$card];
            $buckets[$card] = $count ? $count + 1 : 1;
        }

        $res = 0;
        foreach($buckets as $key => $value) {
            $res = $this->gcd($res, $value);
        }

        return $res > 1;
    }

    function gcd($a, $b) {
        return $b > 0 ? $this->gcd($b, $a % $b) : $a;
    }
}