/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 * optimal for php language
 */
var fairCandySwap = function(A, B) {
    let suma = reducer(A)
    let sumb = reducer(B)



    let diff = (suma - sumb) / 2

    for (let i=0; i< B.length; i++){
        let curr = B[i] + diff
        if(A.includes(curr)) return [curr, B[i]]
    }
};

function reducer(A) {
    return A.reduce((total, amount)=>total+amount);
}

