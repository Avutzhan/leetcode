/**
 * @param {number} n
 */
var OrderedStream = function(n) {
    this.arr = new Array(n);
    this.index = 0;
};

/**
 * @param {number} id
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function(id, value) {
    this.arr[id - 1] = value;
    const result = [];
    while (this.arr[this.index]) {
        result.push(this.arr[this.index++]);
    }
    return result;
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(id,value)
 */
