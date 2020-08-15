# FractionToDecimal

> Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
> 
> If the fractional part is repeating, enclose the repeating part in parentheses.
> 
> If multiple answers are possible, just return any of them.
> 
> Example 1:
> 
> Input: numerator = 1, denominator = 2
> Output: "0.5"
> Example 2:
> 
> Input: numerator = 2, denominator = 1
> Output: "2"
> Example 3:
> 
> Input: numerator = 2, denominator = 3
> Output: "0.(6)"

## Some thoughts

### The method to find the repeating part

I have tried several methods to find out the algorithms, maybe, I should try to solve some corresponding leetcode problem related to this topic first.

1. The 1st methoed that I have tried is to search the pattern in the string as below. Take value 0.012012012 as example. This method can only find the pattens that starts immediately after the '.'. For other cases, it doesn't work at all.
`0 vs 1 01 vs 20 012 vs 012 ...`
2. Search from the end of the string. The assumption is that, the part close to the end (not possible to the end since it is recurring decimal) is more possible to be the recurring part, for example, 0.789012012012... . This method comes to my mind due to method 1 doesn't work. But, this method has the limitation that, the native / will handle the some dig of the repeating part specially. For example, 1/90, it should be **0.01111111111111111**, but actually, the result turns out to be **0.011111111111111112**. For this case, method 2 doesn't work.

**Both method 1 and method 2 are based on facts that I used the native / method to calculate the result.**

So, I need to find another way to calculate **division** by myself (just get rid of the native **/**). I use the way to handle division when I was in primary school, implementing all the details needed for a hand-writen division.

During the process, another way to check the repeating part came to mind. I noticed that combination of (quotient, remainder) kept repeating.

So, the question goes to, how to find out all the repeating combination. It is dictionary. If I found the patten/combination in the dictionary, it means, something repeating start to happen. And please note, the repeating part don't have to just contain a single digit, it can be a combination of several digits, such as 0.012012012...
On the other hand, there should be a way to avoid find out fake repeating pattern, for example, 012012, instead of the atom repeating pattern 012. Use the value corresponding to the key (quotient, remainder) as a mark to represent whether the repeating part has been counted in already.

``` python
if (temp:= mapping.get((inte, remain))) != None:
    if temp != True:
        mapping[(inte, remain)] = True
        repeating += str(inte)
    else:
        break
        # print("repeating {}".format(repeating))
else:
    mapping[(inte, remain)] = False
```

### // and signal

I have noticed that negative value and positive value can generate result when use **//** to get divided by positive number:

```
50//8 = 6
-50//8 = -7 not -6, why???
```

#### The meaning of **//** in Python.