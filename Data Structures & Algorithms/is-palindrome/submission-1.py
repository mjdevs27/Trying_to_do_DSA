class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s if c.isalnum())
        s_final = cleaned.lower()
        chars = list(s_final)
        i = 0
        j = len(chars)-1
        count = (len(chars)+1)//2 
        for k in range(len(chars)):
            if j>=i:
                if chars[i] is chars[j]:
                    i = i + 1
                    j = j - 1 
                    count = count - 1 

        return count ==0 




