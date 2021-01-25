/**
 * @param {number} n
 * @param {number} m
 * @param {number[][]} indices
 * @return {number}
 */
var oddCells = function(n, m, indices) {
    const rowCount = new Uint8Array(n);
    const columnCount = new Uint8Array(m);
    let ret = 0;

    for (let i = 0; i < indices.length; i++) {
        rowCount[indices[i][0]]++;
        columnCount[indices[i][1]]++;
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if ((rowCount[i] + columnCount[j]) % 2 != 0) {
                ret++;
            }
        }
    }

    return ret;
};