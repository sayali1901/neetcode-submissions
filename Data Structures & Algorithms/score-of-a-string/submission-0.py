class Solution:
    def scoreOfString(self, s: str) -> int:

        total = 0 
        n=len(s)

        for i in range(n-1):
            a = abs(ord(s[i+1])- ord(s[i]))
            total +=a 
        

        return total
        