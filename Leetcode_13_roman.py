def romanToInt(s: str) -> int:
    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    s = s.replace('IV','IIII') \
        .replace('XL','XXXX') \
        .replace('XC','LXXXX') \
        .replace('IX','VIIII') \
        .replace('CD','CCCC') \
        .replace('CM','DCCCC')

    for s1 in s:
        ans += rom_int[s1]
    return ans
print(romanToInt('MMMCMXCIX'))

