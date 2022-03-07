<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $pieces
     * @return Boolean
     */
    function canFormArray($arr, $pieces) {
        $map = [];
        foreach ($pieces as $subArray) {
            $map[implode('-', $subArray)] = false;
        }

        $currentPiece = [];
        for ($i = 0; $i < count($arr); $i++) {
            $currentPiece[] = $arr[$i];
            $key = implode('-', $currentPiece);
            if (isset($map[$key]) && $map[$key] === false) {
                $map[$key] = true;
                $currentPiece = [];
            }
        }

        if (!empty($currentPiece)) {
            return false; // we have something from array, for which we found no match
        }
        foreach ($map as $wasUsed) {
            if (!$wasUsed) {
                return false;
            }
        }

        return true;
    }
}