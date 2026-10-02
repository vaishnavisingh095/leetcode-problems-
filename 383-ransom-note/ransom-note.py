from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)
        for letter in ransom_count:
            if magazine_count[letter] < ransom_count[letter]:
                return False
        return True

        
        

