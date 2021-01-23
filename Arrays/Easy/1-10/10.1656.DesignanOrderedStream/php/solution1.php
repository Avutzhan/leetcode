<?php
//best solution simple

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

        while ($this->arr[$this->index] != null) {
            $result[] = $this->arr[$this->index];
            $this->index++;
        }

        return $result;

    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * $obj = OrderedStream($n);
 * $ret_1 = $obj->insert($id, $value);
 * $ret_2 = $obj->insert($id, $value);
 * $ret_3 = $obj->insert($id, $value);
 */