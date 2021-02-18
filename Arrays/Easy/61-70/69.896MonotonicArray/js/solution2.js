/**
 * @param {number[]} A
 * @return {boolean}
 * better solution
 */
var isMonotonic = function(A) {
    let n = A.length;


    if (n <= 2) {
        return true;
    }

    let isGreat = false;
    let isLess = false;

    for (let i = 1; i < n; i++) {
        if (A[i - 1] > A[i]) {
            isGreat = true;
        }

        if (A[i - 1] < A[i]) {
            isLess = true;
        }

        if (isGreat && isLess) {
            return false;
        }


    }


    return true;
};