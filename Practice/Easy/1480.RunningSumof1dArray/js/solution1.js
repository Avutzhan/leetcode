//best solution simple
const runningSum = nums => {
    let running = 0;
    let sum = [];

    for (let i = 0; i < nums.length; i++) {
        running += nums[i];
        sum[i] = running;
    }
    return sum;
}

runningSum([1,2,3,4]); //[1,3,6,10]
// Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

//step 1
//0.Problem + 1 = 1
//step 2
//1 + 2 = 3
//step 3
//3 + 3 = 6
//step 4
//6 + 4 - 10