class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        lstS = list(s)
        idx = -1

        for i in range(len(s) - 1, -1, -1):
            found = False
            cur = s[i]
            ordC = ord(cur)

            if ordC - ord("a") >= k - 1:
                continue

            for nextOrd in range(ordC + 1, ord("a") + k):
                newCur = chr(nextOrd)
                prev = lstS[i - 1] if i > 0 else None
                prev_2 = lstS[i - 2] if i > 1 else None

                # Check for palindrome
                if newCur != prev and newCur != prev_2:
                    found = True
                    lstS[i] = newCur
                    idx = i
                    break

            if found:
                break

        # Fill remaining with valid smallest characters
        if idx != -1:
            for i in range(idx + 1, len(lstS)):
                for c in range(k):
                    ch = chr(ord("a") + c)
                    prev = lstS[i - 1] if i > 0 else None
                    prev_2 = lstS[i - 2] if i > 1 else None
                    if ch != prev and ch != prev_2:
                        lstS[i] = ch
                        break

        res = "".join(lstS)
        return res if res != s else ""
