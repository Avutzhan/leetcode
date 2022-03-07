// T and M: O(n)
func containsDuplicate(nums []int) bool {
    hash := make(map[int]bool)
    for _, v := range nums {
        if _, ok := hash[v]; ok {
            return true
        }
        hash[v] = true
    }
    return false
}

