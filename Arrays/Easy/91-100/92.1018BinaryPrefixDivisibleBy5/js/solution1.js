/**
 * @param {number[]} A
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(A) {
    let cur = 0;
    const r = []

    for (const a of A) {
        cur = ((cur << 1) | a) % 5;
        r.push(cur === 0);
    }

    return r;
};