class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # s= sorted(s)
        # t= sorted(t)

        # if s == t:
        #     return True 
    
        # return False

        letter_counts1 = {}
        letter_counts2 = {}

        for letter in s:
            if letter in letter_counts1:
                letter_counts1[letter] += 1  
            else:
                letter_counts1[letter] = 1   
        
        for letter in t:
            if letter in letter_counts2:
                letter_counts2[letter] += 1  
            else:
                letter_counts2[letter] = 1 
        
        if letter_counts1 == letter_counts2:
            return True 
        
        return False











        
        
    

        