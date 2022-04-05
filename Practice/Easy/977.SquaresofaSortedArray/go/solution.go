func sortedSquares(nums []int) []int {
    res := []int{}
    for _, v := range nums {
        res = append(res, v * v)
    }
    sort.Ints(res)
    return res
}