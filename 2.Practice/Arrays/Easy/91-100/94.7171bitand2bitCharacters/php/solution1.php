<?php

class Solution {

    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits) {
        $isMidCharacter = false;
        for($i = 0; $i < count($bits) - 1; $i++){
            $isMidCharacter = ($bits[$i] === 1 && !$isMidCharacter);
        }
        return !$isMidCharacter;
    }
}