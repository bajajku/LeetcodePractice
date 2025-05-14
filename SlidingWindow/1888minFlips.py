class Solution:
    def minFlips(self, s: str) -> int:
        
        n = len(s) # we save this length as it is length of window
        s += s #we add this string because we can have any possibility like s[0]->s[n-1] or s[2]->s[n+1]meaning is that any continous variation with n length ... 
        ans = float("inf") #assiging the answer max possible value as want our answer to be minimum so while comparing min answer will be given 
        ans1,ans2=0,0#two answer variables telling amount of changes we require to make it alternative
        s1 = ""#dummy string like 10010101
        s2 = ""#dummy string like 01010101
        for i in range(len(s)):
            if i%2==0:
                s1+="1"
                s2+="0"
            else :
                s1+="0"
                s2+="1"
        # for i in range(len(s)):

        #     if s[i] != s1[i]:
        #         ans1 += 1
            
        #     if s[i]!=s2[i]:
        #         ans2 += 1

        #     if i >= n:
        #         if s[i - n] != s1[i - n]:
        #             ans1 -= 1
        #         if s[i - n] != s2[i - n]:
        #             ans2 -= 1 

        #     if i >= n - 1:
        #         ans = min(ans, ans1, ans2)
        
        # return ans

        l, r = 0, 0

        while r < len(s):

            if s[r] != s1[r]:
                ans1 += 1
            if s[r] != s2[r]:
                ans2 += 1
            
            if (r - l + 1) > n:
                if s[l] != s1[l]:
                    ans1 -= 1
                if s[l] != s2[l]:
                    ans2 -= 1
                l += 1
            
            if (r - l + 1) == n:
                ans = min(ans, ans1, ans2)
            
            r += 1
        return ans
            
