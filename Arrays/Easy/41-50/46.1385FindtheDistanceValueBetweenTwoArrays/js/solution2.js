/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    let length1 = arr1.length;
    let length2 = arr2.length;

    let distance = length1;

    for(let i=0; i<length1; i++){
        for(let j=0; j<length2; j++){
            if(Math.abs(arr1[i] - arr2[j]) <= d){
                distance -= 1;
                break;
            }
        }

    }

    return distance;
};