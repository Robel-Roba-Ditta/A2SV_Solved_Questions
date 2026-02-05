class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = []

        for n in nums:
            if n in seen:
                duplicates.append(n)
            else:
                seen.add(n)

        return duplicates
