class Solution:

    def majorityElement(self, nums):
        count = Counter()
        for num in nums:
            count[num] += 1
            if len(count) == 3:
                new_count = Counter()
                for elem, freq in count.items():
                    if freq != 1: new_count[elem] = freq - 1
                count = new_count

        cands = Counter(num for num in nums if num in count)
        return [num for num in cands if cands[num] > len(nums) / 3]