/**
 * @param {number[][]} dominoes
 * @return {number}
 */
var numEquivDominoPairs = function(dominoes) {
    let map = new Map();
    let count = 0;
    for (let [a , b] of dominoes) {
        let key = a < b ? `${a}${b}` : `${b}${a}`;

        if (map.has(key)) {
            let currentIndex = map.get(key) + 1;
            map.set(key, currentIndex);
            count += currentIndex;
        } else {
            map.set(key, 0);
        }
    }

    return count;
};