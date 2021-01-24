/**
 * @param {number[]} arr
 * @return {number}
 */
var sumOddLengthSubarrays = function(arr) {
    let result = 0;

    for(let i = 0; i < arr.length; i++) {
        let currSum = 0;

        for(let j = i; j < arr.length; j++) {
            currSum += arr[j];
            if ((j - i + 1) % 2 == 1) result += currSum;
        }
    }

    return result;
};