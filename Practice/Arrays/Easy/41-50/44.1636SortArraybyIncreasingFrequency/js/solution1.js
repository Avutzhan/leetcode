/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(A) {
    let m = new Map();
    A.forEach(x => m.set(x, 1 + (m.get(x) || 0)));
    let P = [...m.entries()].sort((a, b) => a[1] == b[1] ? b[0] - a[0] : a[1] - b[1]);
    return _.flatten(P.map(([x, cnt]) => Array(cnt).fill(x)));
};