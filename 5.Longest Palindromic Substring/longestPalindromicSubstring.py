'''
Initial Intuition:
-> I have previously have seen this question so my initial intuition was to use this two pointers approach.
-> I realized that each single character(like "a") is a palindrome and if we add same character on its left and right
like ("bab") it is a palindrome.
-> I realized another case "bb" is a palindrome, but I am not sure how to check this in code.
-> Probably looping to find all substring
'''
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    res = ""

    for i in range(len(s)):
        # for odd cases
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if(right - left + 1) > len(res):
                res = s[left: right + 1]
            
            left -= 1
            right += 1

        # for even cases
        left, right = i, i + 1 # taking two initial chars
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if(right - left + 1) > len(res):
                res = s[left: right + 1]
            
            left -= 1
            right += 1
    
    return res


'''
Solution:
-> So actual solution follows the same approach, but using for loop to iterate over each character is what I didnot thought of.
-> So in this solution we do odd case (like "a", "aca") and even cases primarily like ("bb"), and find these palindromic substring 
using initial logic and update if reslen < newly found substring.

'''

'''
Key Takeaways:
1) Use of first for loop is brilliant, I didnt thought of that.
2) Doing odd and even makes so much sense, I dont knwo why I wasn't able to think that.
3) Overall intuition was 50 % correct but implementation needs some work.

'''

        


    