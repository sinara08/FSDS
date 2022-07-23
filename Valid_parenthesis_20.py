def isValid( s: str) -> bool:
    from collections import Counter

    s_valid = ['(', ')', '{', '}']

    for i in range(len(s)):
        if s[i] in s_valid:
            cnt = Counter(s)
            s1_cnt = cnt[s[i]]
            if s[i] == '(' and cnt[')'] == s1_cnt and s[i+1] == ')':
                flag = True
            elif s[i] == ')' and cnt['('] == s1_cnt and s[i-1] == '(':
                flag = True
            elif s[i] == '{' and cnt['}'] == s1_cnt and s[i+1] == '}':
                flag = True
            elif s[i] == '}' and cnt['{'] == s1_cnt and s[i-1] == '{':
                flag = True
            elif s[i] == '[' and cnt[']'] == s1_cnt and s[i+1] == ']':
                flag = True
            elif s[i] == ']' and cnt['['] == s1_cnt and s[i-1] == '[':
                flag = True
            else:
                return False
        else:
            return False

    return flag

tocheck="()[]{}"
print(isValid(tocheck))