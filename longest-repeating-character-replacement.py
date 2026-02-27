class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        tot = 0

        left = 0
        for right in range(len(s)):
            arr[ord(s[right]) - ord('A')] += 1
            tot = max(tot, arr[ord(s[right]) - ord('A')])

            if (right - left + 1) - tot > k:
                arr[ord(s[left]) - ord('A')] -= 1
                left += 1

        return len(s) - left 
