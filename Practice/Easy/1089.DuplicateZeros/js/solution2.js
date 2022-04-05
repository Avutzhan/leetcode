/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    let copy = [...arr];
    let counter = 0;

    for (let i = 0; i < copy.length; i++) {
        if (copy[i] == 0) {
            arr.splice(i + counter, 0, 0);
            counter++;
            arr.pop();
        }
    }

};