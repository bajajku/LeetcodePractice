'''
Initial Intuition:
-> Can use the same logic of even and odd palindrom as we did in longest palindrome before.
-> This question considers "aaa" as 3 separate a's so we can save them as a
dictionary MAP = {(l, r): anything}
-> And return the length for the MAP, this will consider all strings.

Time Complexity : O(n^2) as loop inside loop kinda
Space Complexity: O(n) using a dictionary to save the results.

'''
'''
"abba"
i, j = 3
s[i] = s[j]

'''

def countSubstrings(s: str) -> int:
    
    # MAP = {} #{(l, r): palindrome}
    res = 0
    for i in range(len(s)):

        # Odd cases 
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # if((l, r) in MAP):
            #     continue
            # MAP[(l, r)] = s[l: r+1]

            res += 1
            l -= 1
            r += 1
        
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # if((l, r) in MAP):
            #     continue
            # MAP[(l, r)] = s[l: r+1]

            res += 1
            l -= 1
            r += 1
        
    # return len(MAP)
    return res

'''
Actual solution:
-> It uses a single result variable, instead of dictionary as there will not be repeated
cases in odd and even checks that I thought will be the case.

Time Complexity : O(n^2) as loop inside loop kinda
Space Complexity: O(1) no data structure.

'''  

'''
Key Takeaway:
-> Intuition was in correct direction as it's quite similar to last problem.
-> Just need to understand the algorithm more intuitively in order to prevent that silly mistake.

'''


'''
Another DP solution not the easiest but definitely interesting to look at,

Time Complexity : O(n^2) as loop inside loop kinda
Space Complexity: O(n^2) as we are creating a 2D array of size (n x n).
'''
def countSubstrings(s: str) -> int:

    res = 0
    n = len(s)

    # creating a 2D array of size (n x n).
    memo = [[False] * n for _ in range(n)]

    # iterating reverse 
    for i in range(n-1, -1, -1):
        # checking like "abba"
        # [a] when i, j = 3 | [b, ba] when i = 2, j = 2, 3 | [b, bb, bba] when i = 1, j = 1, 2, 3
        for j in range(i, n):
            # condition 1: end chars of string should be same in palindrome
            # condition 2: either there is no character in between OR the character in between are already marked as palindrome
            if(s[i] == s[j] and (j - i <= 2 or memo[i+1][j-1] == True)):

                # setting index as Palindrome
                memo[i][j] = True
                res += 1

    return res
