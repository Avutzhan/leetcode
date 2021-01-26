/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let n = mat.length;

    let m = Math.floor(n / 2);

    console.log(m);

    let res = 0;

    for (let i = 0; i < n; i++) {
        res += mat[i][i];
        res += mat[n - 1 - i][i];
    }

    if (n % 2 == 1) {
        res -= mat[m][m];
    }

    return res;
};