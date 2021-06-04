//reference js solution

func kidsWithCandies(candies []int, extraCandies int) []bool {
    var max int
    for i:=0; i<len(candies); i++ {
        if candies[i] > max {
            max = candies[i]
        }

    }

    var res []bool
    for i:=0; i<len(candies); i++ {
        if (candies[i] + extraCandies >= max) {
            res = append(res, true)
        } else {
            res = append(res, false)
        }
    }

    return res


}