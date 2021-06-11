/**
 * @param {number[]} A
 * @return {boolean}
 */
var isMonotonic = function(A) {
    let arrLength = A.length;

    let isIncreasing = false;
    let isDecreasing = false;

    for(let i = 1; i <arrLength; i++){
        if(isIncreasing && isDecreasing){
            return false;
        }

        if(A[i] > A[i-1]){
            isIncreasing = true;
        } else if(A[i] < A[i-1]){
            isDecreasing = true;
        }
    }

    return !(isIncreasing && isDecreasing);
};