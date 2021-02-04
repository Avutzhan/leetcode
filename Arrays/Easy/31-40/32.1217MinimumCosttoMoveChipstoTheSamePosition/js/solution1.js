/**
 * @param {number[]} position
 * @return {number}
 */
var minCostToMoveChips = function(position) {
    let odd = 0;

    for (let i = 0; i < position.length; i++) {
        if (position[i] %2) odd++;
    }

    return Math.min(position.length - odd, odd);
};