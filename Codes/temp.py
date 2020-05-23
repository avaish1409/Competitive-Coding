class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res =""
        r = numRows
        ms = -2 + 2*r
        c = len(s)//ms
        for i in range(r):
            for j in range(c+1):
                # res += s[i + 2*ms - 2*(i-1)]
                # res += s[i + 2*ms]
                try:
                    if i+ms*j -2*i>=0:       # and res[-1] != s[i+ms*j - 2*i]
                        res += s[i+ms*j -2*i]
                except:
                    pass
                try:
                    if i+ms*j >= 0 and i != 0 and i != r-1:
                        res += s[i+ms*j]
                except:
                    pass
                print(i+ms*j -2*i,i+ms*j,)
                print(res)
                # print(i + 2*ms - 2*(i-1),i + 2*ms)
            print('\n')
            if len(res)==len(s):
                break
        print(res)
s = Solution()
print(s.convert("PAYPALISHIRING",3))
