/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
const kidsWithCandies = (candies, extraCandies) => {
    const ret = [];
    let max = 0;
    for (const val of candies) {
        if (val > max) {
            max = val
        }
    }
    for (let i = 0; i < candies.length; ++i) {
        ret.push(candies[i] + extraCandies >= max);
    }
    return ret;
};