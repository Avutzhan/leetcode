/**
 * @param {number} lowLimit
 * @param {number} highLimit
 * @return {number}
 */
var countBalls = function(lowLimit, highLimit) {
    let obj = {}

    for(let i = lowLimit; i <= highLimit; i++){
        if(obj[sumDigit(i)] > 0){
            obj[sumDigit(i)]++
        } else {
            obj[sumDigit(i)] = 1
        }
    }

    return Math.max(...Object.values(obj))


};

function sumDigit(num){
    let sum = 0

    while(num){
        sum += num % 10
        num = Math.floor(num / 10)
    }

    return sum
}