#Given a signed 32-bit integer x, return x with its digits reversed.
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        xoriginal = x
        x1 = abs(x)
        finalstring = ''
        y = []
        for i in range(len(str(x1))):
            out = x1%10
            x1 = x1//10
            y.append(out)
            print(y,xoriginal)
        finalstring = ''.join(map(str,y))
        if x < 0:
            return(0-int(finalstring))
        else:
            return(int(finalstring))

instance1 = (Solution(int(43222)))
instance1.Solution
