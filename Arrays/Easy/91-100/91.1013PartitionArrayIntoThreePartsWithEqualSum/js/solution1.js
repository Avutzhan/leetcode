/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canThreePartsEqualSum = function(A) {
    let sum = A.reduce((acc,x)=>acc+x,0)/3;

    let s = 0, count=0;
    for(i=0;i<A.length;i++){
        s+=A[i];
        if(s===sum) {++count; s=0};
    }
    return count>=3;
};