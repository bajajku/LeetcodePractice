class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        # result to store variables
        res = []

        # variables to store line, and length of the line
        line, length = [], 0


        i = 0
        while i < len(words):
            
            # if length of current line + (1 space for each word) + nextWord exceeds maxWidth
            # then we have to append our current line to result
            if((length + len(line) + len(words[i])) > maxWidth):
                
                # calculating extra spaces required to complete the line.
                extra_space = maxWidth - length

                # x is number of words that we need to divide spaces for.
                x = len(line) - 1 if len(line) > 1 else 1

                # spaces = space for each word.
                spaces = extra_space // x
                # there might be a case we have remainder after equally distributing spaces.
                remainder = extra_space % x

                # Add spaces  to the line now
                for j in range(x):
                    line[j] += " " * spaces
                    if(remainder):
                        line[j] += " "
                        remainder -= 1
                
                res.append("".join(line))

                # reset the line and length for further use.
                line,length = [], 0

            # start building new line
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # as our loop will end before last line is added to the result
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        last_line += " " * trail_space

        res.append(last_line)

        return res
        
