/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(A, k) {
    for (let i=-k-1,  j=0; j<A.length; j++) {
        if (A[j] == 1) {
            if (j-i-1 < k )
                return false;
            i = j;
        }
    }
    return true;
};