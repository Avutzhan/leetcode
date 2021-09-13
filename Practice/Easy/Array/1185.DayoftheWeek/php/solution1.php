<?php

class Solution {

    /**
     * @param Integer $day
     * @param Integer $month
     * @param Integer $year
     * @return String
     */
    function dayOfTheWeek($day, $month, $year) {
        $timestamp = strtotime("{$year}-{$month}-{$day}");
        return date('l', $timestamp);
    }
}