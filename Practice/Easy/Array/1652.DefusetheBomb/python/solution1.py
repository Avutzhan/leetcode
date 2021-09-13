class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0] * len(code)

        if k > 0:
            for i in range(len(code)):
                count = 0
                j = i + 1
                while count < k:
                    if j == len(code):
                        j = 0
                    res[i] += code[j]
                    count = count + 1
                    j+=1

        if k < 0:
            for i in range(len(code)):
                count = 0
                j = i - 1
                while count > k:
                    if j == -1:
                        j = len(code) - 1
                    res[i] += code[j]
                    count = count - 1
                    j-=1

        return res
