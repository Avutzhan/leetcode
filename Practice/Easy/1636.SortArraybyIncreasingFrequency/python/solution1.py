class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # 0.Problem) Collect all number and its frequency
        fv_dict = {}  # key as number, value as [frequency, number]
        for n in nums:
            if n in fv_dict:
                fv_dict[n][0] += 1
            else:
                fv_dict[n] = [1, n]

        # 1) Sorting them
        sorted_fv = sorted(fv_dict.values(), key=lambda t: (t[0], t[1]*-1))
        # default, sorted in descending order by frequency and then tne number itself

        # 2) Compose the answer
        ans = []
        for f, v in sorted_fv:
            ans.extend([v]*f)

        # 3) Return it
        return ans