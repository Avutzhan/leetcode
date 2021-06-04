//reference js solution 1
func runningSum(nums []int) []int {
    sum := make([]int, len(nums)+1)

    for i:=1; i<=len(nums); i++ {
       sum[i] = sum[i-1] + nums[i-1]

    }

    return sum[1:]

}