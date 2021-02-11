<?php

class Solution {

    /**
     * @param String[][] $board
     * @return Integer
     */
    function canCapture($board, $i, $j) {
        $captures = 0;
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];

        foreach ($dirs as $dir) {
            $r = $i + $dir[0];
            $c = $j + $dir[1];

            while ($r >= 0 && $r < 8 && $c >= 0 && $c < 8) {
                if ($board[$r][$c] === 'p') { $captures++; }
                if ($board[$r][$c] !== '.') { break; }

                $r += $dir[0];
                $c += $dir[1];
            }
        }

        return $captures;
    }

    function numRookCaptures($board) {
        for ($i = 0; $i < 8; $i++) {
            for ($j = 0; $j < 8; $j++) {
                if ($board[$i][$j] === 'R') {
                    return $this->canCapture($board, $i, $j);

                }
            }
        }
    }
}

