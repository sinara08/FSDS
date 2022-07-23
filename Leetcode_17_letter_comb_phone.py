def letterCombinations(digits: str):
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqsrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backTracking(i, currentStr):
        if len(currentStr) == len(digits):
            res.append(currentStr)
            return
        for c in digitToChar[digits[i]]:
            backTracking(i + 1, currentStr + c)

    if digits:
        backTracking(0, "")

    return res

print(letterCombinations('234'))