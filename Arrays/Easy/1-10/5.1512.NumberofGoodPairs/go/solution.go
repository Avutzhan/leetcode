//reference js solution1

func numIdenticalPairs(nums []int) int {
    var sum int

    for i:=0; i < len(nums); i++ {
        for j:=i+1; j<len(nums); j++ {
            if nums[i] == nums[j] {
                sum++
            }
        }
    }

    return sum
}