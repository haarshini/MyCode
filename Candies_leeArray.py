class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ls =[]
        l = len(candies)
        for i in range(l):
            if candies[i] + extraCandies >= max(candies):
                ls.append(True)
            else:
                ls.append(False)
        return ls