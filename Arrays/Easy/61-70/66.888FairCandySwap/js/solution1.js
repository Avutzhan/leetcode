/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var fairCandySwap = function(A, B) {
    let aliceArr = A;
    let bobArr = B;
    let aliceSize = 0;
    let bobSize = 0;
    let swap = [];

    for (let i = 0; i < aliceArr.length; i++) {
        aliceSize += aliceArr[i];
    }

    for (let i = 0; i < bobArr.length; i++) {
        bobSize += bobArr[i];
    }

    let difference = aliceSize - bobSize;

    for (let i = 0; i < aliceArr.length; i++) {
        for (let j = 0; j < bobArr.length; j++) {
            if ((aliceArr[i] - bobArr[j]) === (difference/2)) {
                swap.push(aliceArr[i], bobArr[j]);
                return swap;
            }
        }
    }

    return swap;
};