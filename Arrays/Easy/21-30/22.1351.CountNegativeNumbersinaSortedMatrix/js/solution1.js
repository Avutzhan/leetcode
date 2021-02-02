/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    let r = m - 1;
    let c = 0;
    let cnt = 0;

    while (r >= 0 && c < n) {
        if (grid[r][c] < 0) {
            r--;
            cnt += n - c;
        } else {
            c++
        }
    }

    return cnt;
};