class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440: #if the length of 𝑡𝑖𝑚𝑒𝑃𝑜𝑖𝑛𝑡𝑠 exceeds 1440, return 0
            return 0
        nums = sorted(int(x[:2]) * 60 + int(x[3:]) for x in timePoints)
        nums.append(nums[0] + 1440)
        return min(b - a for a,b in pairwise(nums))
    # time complexity is 𝑂(𝑛log𝑛)
    # space complexity is 𝑂(𝑛)