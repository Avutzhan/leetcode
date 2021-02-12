class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        answer = []

        counter = collections.Counter(nums)

        pre_flat = sorted(list(counter.items()), key = cmp_to_key(lambda a, b: b[0] - a[0] if a[1] == b[1] else a[1] - b[1]))

        for x, counter in pre_flat:
            answer.extend([x] * counter)
        return answer