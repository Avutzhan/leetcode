/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var shiftGrid = function(grid, k) {
    let cols = grid[0].length;
    let rows = grid.length;
    let len = cols * rows;
    let items = [];
    let newGrid = [];
    for (let item of grid) {
        items = items.concat(item);
    }

    let step = 0;
    k = k % len;
    while (step < k) {
        let last = items.splice(len - 1, 1)[0];
        items.unshift(last);
        step++;
    }
    for (let i = 0; i < rows; i++) {
        newGrid.push([]);
        for (let j = 0; j < cols; j++) {
            newGrid[i].push(items[i * cols + j]);
        }
    }


    return newGrid;
};