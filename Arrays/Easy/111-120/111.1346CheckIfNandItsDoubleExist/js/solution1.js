/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(array) {
    while (array.length) { // While the array has items
        const n = array.pop() // Get an item and remove it from the array
        // If the double or the half is found stop looking
        if (array.includes(n*2) || array.includes(n/2)) return true
    }
    return false // If we get here we've gone through the whole array without finding a match
};