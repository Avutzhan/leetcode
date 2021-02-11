<?php

class Solution {

    /**
     * @param String[][] $board
     * @return Integer
     */
    function numRookCaptures($board) {
        $x;
        $y;
        $ret = 0;
        for ($i = 0; $i < 8; $i++) {
            for ($j = 0; $j < 8; $j++) {
                if ($board[$i][$j] === 'R') {
                    $x = $i;
                    $y = $j;
                }
            }
        }

        for ($i = $x + 1; $i < 8; $i++) {
            if ($board[$i][$y] === 'B') break;
            if ($board[$i][$y] === 'p') { $ret++; break; }
        }
        for ($i = $x - 1; $i >= 0; $i--) {
            if ($board[$i][$y] === 'B') break;
            if ($board[$i][$y] === 'p') { $ret++; break; }
        }
        for ($i = $y + 1; $i < 8; $i++) {
            if ($board[$x][$i] === 'B') break;
            if ($board[$x][$i] === 'p') { $ret++; break; }
        }
        for ($i = $y - 1; $i >= 0; $i--) {
            if ($board[$x][$i] === 'B') break;
            if ($board[$x][$i] === 'p') { $ret++; break; }
        }
        return $ret;
    }

}

