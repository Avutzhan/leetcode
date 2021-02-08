/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    let myMap= new Map()
    let max = 0;

    //create a map to store frequency counts
    for(let i of arr){
        if(myMap.has(i)){
            myMap.set(i, myMap.get(i)+1);
        }else{
            myMap.set(i,1);
        }
    }

    //loop through map to find lucky numbers and modify the max value
    for(let [index, value] of myMap){
        if(index == value){
            max = Math.max(max,value)
        }
    }

    return max > 0 ? max : -1;
};