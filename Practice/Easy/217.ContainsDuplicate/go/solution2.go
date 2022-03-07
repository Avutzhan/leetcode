// T: O(n log n) M: O(1)
func containsDuplicate(nums []int) bool {
    sort.Ints(nums)
    for i := 1; i < len(nums); i ++ {
        if nums[i] == nums[i - 1] {
            return true

        }
    }
    return false
}