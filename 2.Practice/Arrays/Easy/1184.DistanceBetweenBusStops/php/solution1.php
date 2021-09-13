<?php

class Solution {

    /**
     * @param Integer[] $distance
     * @param Integer $start
     * @param Integer $destination
     * @return Integer
     */
    function distanceBetweenBusStops($distance, $start, $destination) {
        if ($start > $destination) {
            $temp = $destination;
            $destination = $start;
            $start = $temp;
        }

        $output = array_slice($distance, $start, $destination - $start);

        $reduced = array_reduce($output, function($carry, $item){
            $carry += $item;
            return $carry;
        });

        $firstarr = array_slice($distance, $destination);
        $secarr = array_slice($distance, 0, $start);
        $newarr = array_merge($firstarr, $secarr);

        $secreduced = array_reduce($newarr, function($carry, $item){
            $carry += $item;
            return $carry;
        });

        return min($reduced, $secreduced);
    }
}