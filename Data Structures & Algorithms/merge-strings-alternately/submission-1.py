class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_word = []
        m = len(word1)
        n = len(word2)
        if m >= n :
            j = 0 
            for i in range(m):
                if j < n:
                    final_word.append(word1[i])
                    final_word.append(word2[j])
                    j = j + 1 
                else:
                    final_word.append(word1[i:])
                    break
        else:
            j = 0 
            for i in range(n):
                if j < m:
                    final_word.append(word1[j])
                    final_word.append(word2[i])
                    j = j + 1 
                else:
                    final_word.append(word2[i:]) 
                    break

        return "".join(final_word)


