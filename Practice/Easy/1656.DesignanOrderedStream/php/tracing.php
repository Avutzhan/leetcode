<?php

class OrderedStream {
    /**
     * @param Integer $n
     */
    public $index;
    public $arr = [];

    function __construct($n) {
        $this->arr = array_fill(0, $n, null);
        $this->index = 1;
    }

    /**
     * @param Integer $id
     * @param String $value
     * @return String[]
     */
    function insert($id, $value) {
        $this->arr[$id] = $value;

        $result = [];

        print_r("before ");
        print_r($this->index);
        print_r("\n");

        while ($this->arr[$this->index] != null) {
            print_r("in ");
            print_r($this->index);
            print_r("\n");

            $result[] = $this->arr[$this->index];
            $this->index++;
        }
        print_r("after ");
        print_r($this->index);
        print_r("\n");
        print_r($this->arr);

        return $result;

    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * $obj = OrderedStream($n);
 * $ret_1 = $obj->insert($id, $value);
 *
 */
//    before 1
//    after 1
//    Array
//    (
//        [0] =>
//        [1] =>
//        [2] =>
//        [3] => ccccc
//        [4] =>
//    )


//    before 1
//    in 1
//    after 2
//    Array
//    (
//        [0] =>
//        [1] => aaaaa
//        [2] =>
//        [3] => ccccc
//        [4] =>
//    )

//    before 2
//    in 2
//    in 3
//    after 4
//    Array
//    (
//        [0] =>
//        [1] => aaaaa
//        [2] => bbbbb
//        [3] => ccccc
//        [4] =>
//    )

//    before 4
//    after 4
//    Array
//    (
//        [0] =>
//        [1] => aaaaa
//        [2] => bbbbb
//        [3] => ccccc
//        [4] =>
//        [5] => eeeee
//    )

//    before 4
//    in 4
//    in 5
//    after 6
//    Array
//    (
//        [0] =>
//        [1] => aaaaa
//        [2] => bbbbb
//        [3] => ccccc
//        [4] => ddddd
//        [5] => eeeee
//    )

//  [null,[],["aaaaa"],["bbbbb","ccccc"],[],["ddddd","eeeee"]]