//solution 1
const kidsWithCandies = (candies, extraCandies) => {
    const ret = [];
    let max = 0;
    for (const val of candies) {
        val > max && (max = val);
    }
    for (let i = 0; i < candies.length; ++i) {
        ret.push(candies[i] + extraCandies >= max);
    }
    return ret;
};
// solution 2
const kidsWithCandies = (candies, extraCandies) => {
    const max = Math.max(...candies);
    return candies.map(candy => candy + extraCandies >= max);
};
//solution 3
const kidsWithCandies = (candies, extraCandies, max = Math.max(...candies)) => candies.map(candy => candy + extraCandies >= max);