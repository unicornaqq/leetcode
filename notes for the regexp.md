# How to match them

```python
aabaab
a*b
```

Current strategy is to split the a*b to [a, b].
Try to match 'a' and 'b' separately.
The question is which 'a' or 'b' in the original string should be matched to?

The expected result is 'a' matched to the head a of the raw string, and 'b' matched to the tail b of the raw string.

In this case, I would say, the pattern __"a*b"__ won't match the whole string.
It can only match __"aab"__ at the beginning or __"aab"__ at the end.

So, choose left match with index() or right match with rfind(), it won't match anyway, so it doesn't make any difference.

Can I say, for the match case, only one case?
But for the unmatch case, it can match to different substring.

```python
aaaaaab
a*b
```

__"a"__ of pattern match to head of the raw string, and __"b"__ match to the end of the raw string. No matter we use __index()__ or __rfind()__, it can find the only match. Or, in another word, if the match with __index()__ function failed, then the match failed, even if we try to use __rfind()__ afterwards.

__BUT__, for __".*"__, we should consider the case that __index()__ failed to match, but __rfind()__ matched successfully.
