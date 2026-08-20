class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        for i in candies:
            total = extraCandies + i
            if total >= max(candies):
                results.append(True)
            else:
                results.append(False)

        return results