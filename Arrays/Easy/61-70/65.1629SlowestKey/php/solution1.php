<?php

class Solution {

    /**
     * @param Integer[] $releaseTimes
     * @param String $keysPressed
     * @return String
     */
    function slowestKey($releaseTimes, $keysPressed) {
        $k = $keysPressed[0];
        $t = $releaseTimes[0];
        $count = count($releaseTimes);
        for ($i = $count - 1; $i > 0; $i--) {

            $time = $releaseTimes[$i] - $releaseTimes[$i-1];

            if ($time > $t || ($time == $t && $keysPressed[$i] > $k)) {
                $t = $time;
                $k = $keysPressed[$i];
            }

        }

        return $k;

    }
}