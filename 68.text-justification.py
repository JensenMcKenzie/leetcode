#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        returns = []
        currentLine = 0
        currentLineWords = []
        for i in range(len(words)):
            #account for min space needed for new word
            if len(words[i])+ currentLine + len(currentLineWords) -1 >= maxWidth:
                if len(currentLineWords) == 1:
                    returns.append(currentLineWords[0] + (" " * (maxWidth - currentLine)))
                else:
                    extra = (maxWidth - currentLine)%(len(currentLineWords) -1)
                    string = ""
                    for j in range(len(currentLineWords) -1):
                        string += currentLineWords[j] + (" " * (((maxWidth) - currentLine)//(len(currentLineWords) -1)))
                        if extra > 0:
                            string += " "
                            extra -= 1
                    returns.append(string + currentLineWords[-1])
                currentLine = len(words[i])
                currentLineWords = [words[i]]
            else:
                currentLine += len(words[i])
                currentLineWords.append(words[i])
        if len(currentLineWords) == 1:
            print('x')
            returns.append(currentLineWords[0] + (" " * (maxWidth - currentLine)))
        else:
            string = ""
            for j in range(len(currentLineWords)-1):
                string += currentLineWords[j] + " "
            returns.append(string + currentLineWords[-1] + (" " * (maxWidth - len(string) - len(currentLineWords[-1]))))
        return returns
        
# @lc code=end

