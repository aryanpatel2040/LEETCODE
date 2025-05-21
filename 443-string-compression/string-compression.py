class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  
        left = 0  
        for read in range(len(chars)):
           
            if read + 1 == len(chars) or chars[read] != chars[read + 1]:
                chars[write] = chars[left]
                write += 1
                count = read - left + 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                left = read + 1

        return write  