//reference js solution 1

func decompressRLElist(nums []int) []int {
    var result []int

    for i:=1; i< len(nums); i+=2 {
        for j:=0; j<nums[i-1]; j++ {
            result = append(result, nums[i])
        }
    }

    return result
}