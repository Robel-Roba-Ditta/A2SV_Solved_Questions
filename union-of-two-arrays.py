class Solution:
    def findUnion(self, a, b):
        sset1 = set(a)
        sset2 = set(b)

        union_set = sset1 | sset2

        return sorted(list(union_set))
