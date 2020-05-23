class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        print(str)
        flag = 1
        if str[0] == '+':
            str = str[1:]
        elif str[0] == '-':
            str = str[1:]
            flag = -1
        num = ''
        for i in str:
            if i.isnumeric():
                num += i
            else:
                print('break:', i)
                break
        if num == '':
            return 0
        try:
            num = int(flag) * int(num)
            if num < -1 * 2 ** 31 or num > -1 + (2 ** 31):
                print('num:',num)
                return -1 * 2 ** 31
            return num
        except Exception as e:
            print('num', int(num), 'f:', flag)
            print(int(flag)*int(num))
            print(e)
            return -1 * 2 ** 31


s = Solution()
print(s.myAtoi("  -42"))
