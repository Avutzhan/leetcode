const runningSum = nums => {
    let sum = [];
    sum[0] = nums[0];
    for (let i = 1; i < nums.length; i++) {
        // console.log(sum);
        sum[i] = sum[i - 1] + nums[i];
        // console.log(sum[i - 1]);
    }
    return sum;
}

runningSum([1,2,3,4]); //[1,3,6,10]
// Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

//step 1
//sum[0] = 1
//sum[1] = sum[i - 1] prev num is 1 + 2 = 3
//sum = [1, 3]
//step 2
//sum[2] = sum[i - 1] prev num is 3 + 3 = 6
//sum = [1, 3, 6]
//step 3
//sum[3] = sum[i - 1] prev num is 6 + 4 = 10
//sum = [1, 3, 6, 10]
