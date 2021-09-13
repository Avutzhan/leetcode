class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # create an empty list to hold result
        result = []

        # create the permutation
        mList = [x for x in range(1, m + 1)]

        # iterate over each element from queries
        for x in queries:
            # append the index of query value from the permutation
            result.append(mList.index(x))
            # remove the element from the permutataion
            mList.remove(x)
            # add the query element in the begining of the permutation
            mList.insert(0, x)

        # return the stored index result of queries
        return result