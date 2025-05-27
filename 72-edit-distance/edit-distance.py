class Solution:
    @cache
    def minDistance(self, s1: str, s2: str) -> int:
        if s1 == "" or s2 == "":
            return len(s1 + s2)
        elif s1[0] == s2[0]:
            return self.minDistance(s1[1:], s2[1:])
        else:
            return 1 + min(
                self.minDistance(s1, s2[1:]),  # insert
                self.minDistance(s1[1:], s2),  # remove
                self.minDistance(s1[1:], s2[1:]),  # replace
            )