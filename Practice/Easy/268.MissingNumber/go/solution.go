// T: O(n) M: O(1)
func equal(nums []int, v int) bool {
    for i := 0; i < len(nums); i++ {
        if nums[i] == v {
            return true
        }
    }
    return false
}

//T: O(n^2) M: O(n)
func missingNumber(nums []int) int {
    tmp := []int{}
    for i := 0; i < len(nums) + 1; i++ {
        tmp = append(tmp, i)
    }

    var res int
    for i := 0; i < len(tmp); i++ {
        if !equal(nums, tmp[i]) {
            res = tmp[i]
        }
    }

    return res
}