class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_amount = max(candies)

        output = []

        for item in candies:
            if (item + extraCandies) >= max_amount:
                output.append(True)
            else:
                output.append(False)

        return output
