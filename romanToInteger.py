class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val = 0
        past = 0
        for i in s:
            now = ref[i]
            val += now
            if past < now:
                val -= 2*past
            past = now
        return val
