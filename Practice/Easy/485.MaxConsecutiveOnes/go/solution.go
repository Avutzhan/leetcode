func findMaxConsecutiveOnes(nums []int) int {
    var current = 0
    var maximus float64 = 0

    for i := 0; i < len(nums); i++ {
        if nums[i] == 1 {
            current++
            maximus = math.Max(float64(current), float64(maximus))
        } else {
            current = 0
        }
    }

    return int(maximus)
}