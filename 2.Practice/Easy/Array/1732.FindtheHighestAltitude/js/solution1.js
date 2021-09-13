/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let current = 0;
    let maximum = 0;

    for (let i = 0; i < gain.length; i++) {
        current += gain[i];
        maximum = Math.max(maximum, current);
    }

    return maximum;
};