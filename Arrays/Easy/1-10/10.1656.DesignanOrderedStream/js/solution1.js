/**
 * @param {number} n
 */
var OrderedStream = function(n) {
    this.arr = new Array(n);
    this.index = 1;
};

/**
 * @param {number} id
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function(id, value) {
    this.arr[id] = value;
    const result = [];
    while (this.arr[this.index] != undefined) {
        result.push(this.arr[this.index]);
        this.index++;
    }
    return result;
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(id,value)
 * var param_2 = obj.insert(id,value)
 * var param_3 = obj.insert(id,value)
 */