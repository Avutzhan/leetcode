type NumArray struct {
    Nums []int
}


func Constructor(nums []int) NumArray {
    return NumArray{Nums: nums}
}


func (this *NumArray) SumRange(left int, right int) int {
    res := 0
    for i := left; i < right + 1; i++ {
        res += this.Nums[i]
    }

    return res
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(left,right);
 */