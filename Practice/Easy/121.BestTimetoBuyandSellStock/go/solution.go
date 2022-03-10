func maxProfit(prices []int) int {
    maxProfit := 0
    minPrice := math.MaxInt32

    for _, v := range prices {
        minPrice = min(minPrice, v)
        maxProfit = max(maxProfit, v - minPrice)
    }

    return maxProfit
}


func min(a, b int)int{
    if a < b {
        return a
    }
    return b
}

func max(a, b int)int{
    if a > b {
        return a
    }
    return b
}
