class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        r=k-1
        m=0
        c=0
# COUNT VOWELS IN WINDOW L TO R
        for i in s[l:r+1]:
                if i in {'a','e','i','o','u'}:
                    c+=1
        print(c)
        m=max(m,c)
# TAKE WINDOW UNTIL LAST ELEMENT
        while r<len(s)-1:
# WHEN MOVING RIGHT IF THIS ELEMENT IS VOWEL DECREASE BY 1
            if s[l] in {'a','e','i','o','u'}:
                c-=1
            l+=1
# MOVE RIGHT
# WHEN MOVING RIGHT IF NEXT ELEMENT IS VOWEL INCREASE BY 1
            if s[r+1] in {'a','e','i','o','u'}:
                c+=1
            r+=1
# TAKE WHICH WINDOW HAS MORE VOWELS
            m=max(c,m)
        return m

# PLEASE UP[VOTE]