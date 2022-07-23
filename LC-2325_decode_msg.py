import string
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res={}
        op = []
        l = list(string.ascii_lowercase)
        key=key.replace(' ','')
        i=0
        for k in key:
            if k not in res:
                res[k] = l[i]
                i+=1
        #print(res.items())
        for msg in message:
            if msg != ' ':
                op.append(res[msg])
            else:
                op.append(' ')

        return ''.join(op)
s1=Solution()
print(s1.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo","zwx hnfx lqantp mnoeius ycgk vcnjrdb"))