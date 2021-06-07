#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative=False
        
        if x<0:
            isNegative=True
            x=abs(x)
        
        rev=0
        power=len(str(x))-1
        while x > 0:
            rem=x % 10
            rev = (rem * pow(10,power)) + rev
            x = x/10
            power-=1
            
        
        if isNegative:
            rev= (-1 * rev)
            
        return rev if -(2**31)-1 < rev < 2**31 else 0
            
