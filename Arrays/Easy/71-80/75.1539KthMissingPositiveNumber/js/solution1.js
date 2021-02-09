/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    const missing = [];
    const len = arr.length + k;

    /*
      arr = [2,3,4,7,11], k = 5
      arr.length = 5
      At max we only need to check up to len + k:

          say arr = [10, 100, 1111, 22222, 33333], its missing [1, 2, 3, 4, 5]
          we only need to check the kth missing element, which would be 5.

          say arr = [1, 2, 3, 4, 5], its missing [6, 7, 8, 9, 10]
          5th ele = 10;
    */
    for (let i = 0, j = 1; j <= len; j++) {
        arr[i] != j ? missing.push(j) : i++;
        if (missing.length == k) return missing.pop()
    }
};