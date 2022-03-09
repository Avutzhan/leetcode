func findDisappearedNumbers(nums []int) []int {
    ans := []int{}

    for _, v := range nums {
        idx := abs(v) - 1
        if nums[idx] > 0 {
            nums[idx] = -nums[idx]
        }

    }

    for i, v := range nums {
        if v > 0 {
            ans = append(ans, i + 1)
        }

    }

    return ans

}

func abs(n int) int {
    if n > 0 { return n }
    return -n
}