## Analysis

When calculating the m^n, the classic way is usually muliply integer m by n times, which leads to the time complexity of O(n)

But you might think, "ummmmm, what if I can divide those multipliers to a few equivalent-sized groups and multiply the results of these groups afterwards. For instance, if we do, 2^4, instead of calculating 2 * 2 * 2 * 2 = 16, can we do 2 * 2 = 4, then 4 * 4  = 16?

The answer is definitely yes, by using some tricks in recursive programming.