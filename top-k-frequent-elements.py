class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = []
        for i, _ in c.most_common(k):
            l.append(i)

        return l
