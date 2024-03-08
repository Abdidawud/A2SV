class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=s
        left=0
        right=0
        dic_t=Counter(t)
        dic_s=defaultdict(int)
        check=True
        set_t={i:1 for i in dic_t.keys()}
        set_s={}

        while right<=len(s):
            if set_s == set_t and left < right:
                ans = ans if len(ans) <= right - left else s[left:right]
                check = False
                dic_s[s[left]] -= 1
                if dic_s[s[left]] < dic_t[s[left]]:
                    if s[left] in set_s:
                        set_s.pop(s[left])
                    if dic_s[s[left]] == 0:
                        dic_s.pop(s[left])
                left += 1
            elif right < len(s) and s[right] in set_t:
                dic_s[s[right]] += 1
                if dic_s[s[right]] >= dic_t[s[right]]:
                    set_s[s[right]] = 1
                right += 1
            else:
                right += 1
        if check:
            return ""
        return ans