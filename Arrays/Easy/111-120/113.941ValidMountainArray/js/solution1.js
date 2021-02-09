/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(A) {
    let N = A.length,
        i = 0,
        j = N - 1;
    while (i + 1 < N  && A[i] < A[i + 1]) ++i;
    while (0 <= j - 1 && A[j] < A[j - 1]) --j;
    return 0 < i && i == j && j < N - 1;
};