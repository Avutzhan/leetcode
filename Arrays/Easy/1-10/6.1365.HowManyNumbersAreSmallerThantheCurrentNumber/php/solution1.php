<?php
//best solution simple

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallerNumbersThanCurrent($nums) {
        $sorted = $nums;
        sort($sorted);

        for($i = 0; $i < count($nums); $i++) {
            $nums[$i] = array_search($nums[$i], $sorted);
        }

        return $nums;
    }
}

//native php style
class Solution2 {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallerNumbersThanCurrent($nums) {
        $sorted = $nums;
        sort($sorted);

        foreach ($nums as $key => $val) {
            $nums[$key] = array_search($val, $sorted);
        }

        return $nums;
    }
}

//immutable input
class Solution3 {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallerNumbersThanCurrent($nums) {
        $sorted = $nums;
        sort($sorted);
        $res = [];

        foreach ($nums as $key => $val) {
            $res[$key] = array_search($val, $sorted);
        }

        return $res;
    }
}
