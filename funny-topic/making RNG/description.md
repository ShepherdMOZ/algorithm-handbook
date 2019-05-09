## Analysis
Think about this case, how can you generate all number from 1 to n^2, using a function that can only return each integer from 1 to n exactly once?

Suppose the function is:
```
def getint():
    return [1, 2, 3]
```
We can get what we want by using the offsetting calculation:
```
for x in getint():
    for y in getint():
        print(3 * x + y - 3)
```

What happened here? Let's look into the result [1, 2, 3, 4, 5, 6, 7, 8, 9]. You may notice that this can be evenly divide into three parts, [1, 2, 3], [4, 5, 6] and [7, 8, 9]. For [1, 2, 3], each number can be represented by 3*1 + i - 3, i = {1, 2, 3}. For [4, 5, 6],  each number can be represented by 3*2 + i - 3, i = {1, 2, 3}. For [7, 8, 9],  each number can be represented by 3*3 + i - 3, i = {1, 2, 3}

So, we can dirive our findings, giving a set of integers from 1 to n, we can generate all integer from 1 towards n^2 using the formular n*m + i - n (The variable m represents which segment the number is located in, and the variable i represents its position in the segment)

But what if I got [1,2,3] but I only need [1,2,3,4,5]. Still easy, we can achieve this by limiting the the variable m and i. So 4 and 5 is in the second segment and the position of final integer 5 is 2. So we just apply m <= 2 and i <= 2

The situation is pretty similar while 1 to n is given randomly. If we have rand() = random.randint(1,5), we can get any random number from 1 to 7 by applying dice = 5*rand() + rand() -5 first, and if this dice value is not exceed 21, we can then do dice % 7 + 1 to get the random value at the range we want. Otherwise, we just re-roll dice. Well, technically if we use this method, the distribution of number between 1 to 7 is NOT perfectly even. This is beacause 7 is not a multiple of 5.