class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)
        vowel_chars = [ch for ch in s if ch in vowels]

        result = []
        for ch in s:
            if ch in vowels:
                result.append(vowel_chars.pop())
            else:
                result.append(ch)

        return ''.join(result)
