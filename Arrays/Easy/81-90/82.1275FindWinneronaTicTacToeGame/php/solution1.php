<?php

class Solution {

    /**
     * @param Integer[][] $moves
     * @return String
     */
    function tictactoe($moves) {
        $cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];
        $grid = array_fill(0, 9, 0);

        for ($i = 0; $i < count($moves); $i++) {
            $grid[$moves[$i][0] * 3 + $moves[$i][1]] = ($i % 2) + 1;
        }

        for ($i = 0; $i < count($cases); $i++) {
            $role = $grid[$cases[$i][0]];
            if ($role !== 0 && $grid[$cases[$i][1]] === $role && $grid[$cases[$i][2]] === $role) {
                return $role === 1 ? 'A' : 'B';
            }
        }

        return count($moves) === 9 ? 'Draw' : 'Pending';
    }
}