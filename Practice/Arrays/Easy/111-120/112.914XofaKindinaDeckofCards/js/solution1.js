/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    let buckets = new Map();

    deck.forEach ((card) => {
        let count = buckets.get(card);
        buckets.set(card, count ? count+1 : 1);
    });

    let res = 0;
    for (let bucket of buckets.values()) {
        res = gcd(res, bucket);
    }

    return res > 1;
};

function gcd (a, b) {
    return b > 0 ? gcd(b, a % b) : a;
}