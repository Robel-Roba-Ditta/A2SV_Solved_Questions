class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l1 = Counter(ransomNote)
        l2 = Counter(magazine)

        for i, j in l1.items():
            if l2[i] < l1[i]:   
                return False

        return True


        
