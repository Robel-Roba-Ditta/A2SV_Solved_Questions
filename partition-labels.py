class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        l = []
        left = 0
        right= 0
        for i in range(len(s)):
            right= max(right, dic[s[i]])
            if i == right:
                l.append(right- left + 1)
                left = i + 1
        return l
