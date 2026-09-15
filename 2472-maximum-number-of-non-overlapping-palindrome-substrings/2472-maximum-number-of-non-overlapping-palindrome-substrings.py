class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0
        
        while i < n:
            found = False
            for j in range(i + k - 1, min(i + k + 1, n)):
                l = j - k + 1 if (j - i + 1) == k else j - k
                
                sub = s[l : j + 1]
                if sub == sub[::-1]:
                    ans += 1
                    i = j + 1  
                    found = True
                    break
            
            if not found:
                i += 1
                
        return ans