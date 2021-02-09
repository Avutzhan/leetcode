/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    const sorted = arr.slice().sort((a, b) => a - b);

    const rank = {};

    for (let i = 0, r = 0; i < sorted.length; i += 1) {
        if (sorted[i] !== sorted[i - 1]) {
            r += 1;
            rank[sorted[i]] = r;
        }
    }

    return arr.map(v => rank[v]);
};