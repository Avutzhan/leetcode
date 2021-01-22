/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {
    let result = start;
    console.log("n ", n);
    console.log("start ", start);
    console.log("result ", result);

    for (let i = 1; i < n; i++) {
        console.log("i =", i);
        console.log("prev result ", result);
        console.log("nums ", (start + 2 * i));
        result = result ^ (start + 2 * i);


        console.log("curr result ", result);
        console.log("\n\n ");
    }

    return result;
};

xorOperation(5, 0);