//solution 1
const runningSum = nums => {
    nums.reduce((a,c,i,arr) => arr[i] += a)
    return nums
}

// a: accumulator
// c: current value
// i: index
// arr: source array
