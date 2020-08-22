""" Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 231 − 1 when the division result overflows. """

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 1
        sign = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            result = dividend
        else:
            if dividend < divisor:
                result = 0
            elif dividend >= divisor and dividend < (divisor + divisor):
                result = 1
            else:
                # result = self.divide(dividend-divisor-divisor, divisor) + result + result
                # for this case, the dividen is >= 2* divisor
                double_divisor = divisor
                temp = 1
                while (double_divisor << 1) <= dividend:
                    double_divisor = double_divisor << 1
                    temp = temp << 1
                left = dividend - double_divisor
                result = temp + self.divide(left, divisor)
        result = sign * result
        if result > (2**31 - 1) or result < (-2**31):
            return 2**31 - 1
        else:
            return result

sol = Solution()
print(sol.divide(2147483647, 2))
# print(sol.divide(100, 2))

""" -2147483648
-1 """