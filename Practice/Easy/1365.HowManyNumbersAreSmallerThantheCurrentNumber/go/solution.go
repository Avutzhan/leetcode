//reference js solution1

func smallerNumbersThanCurrent(nums []int) []int {
    res := make([]int, len(nums))

    for i:=0; i<len(nums); i++ {
        counter := 0
        for j:=0; j< len(nums); j++ {
            if j == i {continue}
            if nums[i] > nums[j] {counter++}
        }
        res[i] = counter
    }

    return res
}