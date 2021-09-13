/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(A) {
    let M = A.length,
        N = A[0].length,
        cnt = 0;
    let row = Array(M).fill(0),
        col = Array(N).fill(0);
    for (let i = 0; i < M; ++i)
        for (let j = 0; j < N; ++j)
            if (A[i][j])
                ++row[i],
                    ++col[j];
    for (let i = 0; i < M; ++i)
        for (let j = 0; j < N; ++j)
            if (A[i][j] && row[i] == 1 && col[j] == 1)
                ++cnt;
    return cnt;
};