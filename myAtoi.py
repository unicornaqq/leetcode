class Solution:
    def myAtoi(self, str: str) -> int:
        negative = False
        no_digit = True
        char_to_number_map = dict([
            ('0', 0),
            ('1', 1),
            ('2', 2),
            ('3', 3),
            ('4', 4),
            ('5', 5),
            ('6', 6),
            ('7', 7),
            ('8', 8),
            ('9', 9),
            ('-', None),
            ('+', None)
        ])
            
        str = str.strip(' ')
        if len(str) == 0:
            return 0
        if str[0] not in char_to_number_map.keys():
            #print(str[0])
            #print("it is not a number")
            return 0
        if str[0] == '-':
            #print("it is a negative")
            negative = True
            begin = 1
        elif str[0] == '+':
            begin = 1
        else:
            #print("it is a positive")
            begin = 0
        
        cumulative = 0
        for i in range(begin, len(str)):
            if str[i] in char_to_number_map.keys() and char_to_number_map[str[i]] != None:
                # it is a number
                no_digit = False
                cumulative = cumulative*10 + char_to_number_map[str[i]]
            else:
                break
        
        if no_digit == True:
            return 0
        
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff

        if negative and cumulative != 0:
            cumulative = (-1)*cumulative
            val = cumulative & neg_limit
            if(val == neg_limit): 
                #hex:0x80000000, bin:10000000... if the number is within the range, it will be all and out by 0 
                return cumulative
            else:
                return neg_limit
        elif cumulative == 0:
            return cumulative
        else:
            val = cumulative & pos_limit
            if val == cumulative:
                return cumulative
            else:
                return pos_limit
            
sol = Solution()
#print("==1==")
#print(sol.myAtoi("   -1xxxx "))
#print("==2==")
#print(sol.myAtoi("   -1"))
#print("==3==")
#print(sol.myAtoi("   +1"))
#print("==4==")
#print(sol.myAtoi("   1"))
#print("==5==")
#print(sol.myAtoi("   0"))
#print("==6==")
#print(sol.myAtoi("   -0"))
#print("==7==")
#print(sol.myAtoi("   -91283472332 "))
#print("==8==")
#print(sol.myAtoi("   -2147483648 "))
#print("==9==")
#print(sol.myAtoi("   -+1xxxx "))
#print("==10==")
#print(sol.myAtoi("   +-1xxxx "))
#print("==11==")
#print(sol.myAtoi("   xxxx-42"))
#print("==end==")
