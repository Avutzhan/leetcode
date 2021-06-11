/**
 * @param {number[]} arr
 * @return {boolean}
 */
var checkIfExist = function(A) {
    const arr = [];

    for (i = 0; i < A.length; i++) {
        if (arr.indexOf(A[i] * 2) != -1 ||
            arr.indexOf(A[i] / 2) != -1)
            return true;                               // check prev - 1/2*,2* as it is not sorted

        arr.push(A[i]);
    }

    return false;
};