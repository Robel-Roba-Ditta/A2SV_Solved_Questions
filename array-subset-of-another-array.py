class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        sset1 = set(a)
        sset2 = set(b)

        if sset1.issubset(sset2):
            return True
        else:
            return False
