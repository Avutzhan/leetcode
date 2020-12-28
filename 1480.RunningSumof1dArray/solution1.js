//solution 1
const runningSum = nums => {
    // console.log(nums, "input array");
    nums.reduce((a,c,i,arr) => arr[i] += a)
    return nums
}

runningSum([1,2,3,4]); //[1,3,6,10]
// Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

// a: accumulator
// c: current value
// i: index
// arr: source array
