/**
 * @param {number[]} arr
 * @return {number}
 */
var trimMean = function(A) {
    let N = A.length,
        K = Math.floor(N / 20);
    return A.sort((a, b) => a - b).slice(K, N - K).reduce((a, b) => a + b) / (N - 2 * K);
};