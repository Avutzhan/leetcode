/**
 * @param {number} n
 * @return {number}
 */
var countLargestGroup = function(n) {
    let m = new Map(), max = 0;
    for (let i = 1; i <= n; i++) {
        let sum = getSum(i);
        m.set(sum, m.get(sum)+1 || 1);
        max = Math.max(max, m.get(sum));
    }
    return Array.from(m.values()).filter(num => num === max).length;
};

var getSum = function(n) {
    let sum = 0;
    while (n > 0) {
        sum += n % 10;
        n = Math.floor(n / 10);
    }
    return sum;
}