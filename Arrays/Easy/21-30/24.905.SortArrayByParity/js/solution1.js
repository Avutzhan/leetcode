/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {
    const B = [];
    for (let a of A)
        if (a % 2 === 1) B.push(a);
        else B.unshift(a);
    return B;

};