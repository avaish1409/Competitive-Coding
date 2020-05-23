def lengthOfLongestSubstring2(s):
    """
    :type s: str
    :rtype: int
    """

    str_list = []
    max_length = 0
    count = 0

    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x) + 1:]
            count += 1

        str_list.append(x)
        max_length = max(max_length, len(str_list))
        # print(str_list)
    print(count)

    return max_length

def fin(l):
    collect = [l[0]]
    max_l = 0
    flag = 0
    for i in l:
        if i > collect[-1]:
            collect.append(i)
            print('a')
        elif flag == 1:
            flag = 2
            if collect[-2] < min(collect[-1], i) < l[l.index(i)+1]:
                collect[-1] = min(collect[-1], i)
            elif collect[-2] < max(collect[-1], i) < l[l.index(i)+1]:
                collect[-1] = max(collect[-1], i)
            else:
                collect = [i]
                flag = 0
            print('b')
            continue
        else:
            print('c')
            flag += 1
        if flag == 2:
            print("mx",collect)
            max_l = max(max_l, len(collect))
            collect = collect[collect.index(i):]
            flag = 0
        print(collect)
    print(max_l, collect)


# print(lengthOfLongestSubstring2([1,2,5,3,4]))
print(fin([1, 2, 5, 3, 6]))
