/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
    const countMapping = {};
    const solArr = [];
    const restArr = [];

    for (const val of arr2) {
        countMapping[val] = 0;
    }

    for (const val of arr1) {
        if (countMapping[val] >= 0) {
            countMapping[val]++;
        } else {
            restArr.push(val);
        }
    }

    for (const val of arr2) {
        for (let i = 0; i < countMapping[val]; i++) {
            solArr.push(val)
        }
    }

    return [...solArr, ...restArr.sort((a, b) => a > b ? 1 : -1)];
};