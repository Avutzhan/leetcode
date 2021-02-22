<?php

class Solution {

    /**
     * @param Integer[] $flowerbed
     * @param Integer $n
     * @return Boolean
     */
    function canPlaceFlowers($flowerbed, $n) {
        for ($i = 0; $i < count($flowerbed) && $n !== 0; $i++) {
            if (
                $flowerbed[$i] === 0 &&
                $flowerbed[$i - 1] !== 1 &&
                $flowerbed[$i + 1] !== 1
            ) {
                $n--;
                $i++;
            }
        }
        return $n === 0;
    }
}