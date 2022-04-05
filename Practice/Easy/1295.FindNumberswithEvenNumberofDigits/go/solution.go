func findNumbers(nums []int) int {
    count := 0
    for _, v := range nums {
        if digitNumber(v) % 2 == 0 {
            count++
        }
    }

    return count
}

func digitNumber(num int) int {
    count := 0
    for num != 0 {
        num /= 10
        count++
    }
    return count
}