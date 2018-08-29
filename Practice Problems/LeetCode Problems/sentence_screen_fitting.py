# Currently solution exceeds time constraint, use DP to make more efficient

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        count = 0
        row = 1
        col = 0        
        while row*col < rows*cols:
            for word in sentence:
                if len(word) > cols:
                    return 0
                else:
                    if len(word) > cols-col:
                        row += 1
                        col = len(word) + 1
                    else:
                        col += len(word) + 1
            if row > rows:
                return count
            else:
                count += 1
        return count
