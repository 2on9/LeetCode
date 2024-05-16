class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = list(s.split(' '))
        wordList = reversed(wordList)
        for word in wordList:
            if word == '':
                pass
            else:
                return(len(word))
        
            