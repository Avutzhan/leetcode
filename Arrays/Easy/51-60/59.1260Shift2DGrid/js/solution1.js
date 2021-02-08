/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    var arr = grid.flat();
    while (k--) {
        arr.unshift(arr.pop());
    }

    var res = [];
    var len = grid[0].length;
    while (arr.length) {
        res.push(arr.splice(0, len));
    }

    return res;
};