/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var luckyNumbers  = function(matrix) {
    let result = [];
    let maxCol = {};

    // column
    for (let i = 0; i < matrix[0].length; i++) {
        maxCol[i] = matrix[0][i];
        for (let j = 0; j < matrix.length; j++) {
            let column = matrix[j][i];
            if (column > maxCol[i])
                maxCol[i] = column;
        }
    }

    // row
    for (let row = 0; row < matrix.length; row++) {
        let minRow = Math.min(...matrix[row]);
        if (Object.values(maxCol).indexOf(minRow) > -1) {
            result.push(minRow)
        }
    }
    return result;
};