/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(A) {
    let N = A.length;
    let a = A[0],
        b = A[1],
        c = -1;
    for (let i = 2; i < N; ++i, a = b, b = c)
        c = A[i] + Math.min(a, b);
    return Math.min(a, b);
};