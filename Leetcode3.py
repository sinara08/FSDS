def string_display(s):
    lst1 = []
    lst2 = []
    i=0
    j=0

    substr = {}
    longest = 0
    start=0
    length=0

    for i, num in enumerate(s):
        if s[i] in substr and substr[num] >= start:
            length = i - substr[num]
            start = substr[num]+1


            #if len(substr) > longest:
             #   longest = len(substr)
        else:

            length += 1
            max(longest, length)
            if length> longest:
                longest = length
        substr[num] = i



    return longest
    #for i in range(len(str1)):
    #while True:
        #i = j
        # if i < len(str1):
        #     if str1[i] not in lst1:
        #         lst1.append(str1[i])
        #         i+=1
        #     elif len(lst2) < len(lst1):
        #         lst2 = lst1
        #         lst1 = []
        #         #lst1.append(str1[i])
        #         j+=1
        #         i=j
        #     else:
        #         lst1 = []
        #         #lst1.append(str1[i])
        #         j += 1
        #         i= j
        #
        # else:
        #     break


        #j+=1

    #lst = lst2 if len(lst2) > len(lst1) else lst1
    #print(''.join(lst))
    #return len(lst)


my_str = 'dvdf'
print(my_str)
print(string_display(my_str))
