## Analysis

Think about a simply version of this question [2, 2, 5, 2]

It is indeed difficult to find the '5' that is shown up exactly once, in decimal place...

But, if we re-visit this issue using binary version:

| Num / Bit | 3 | 2 | 1 | 0 |
| ---- | :-:| :-: | :-: | :-: |
| 2 | 0 | 0 | 1 | 0 | 
| 2 | 0 | 0 | 1 | 0 | 
| 5 | 0 | 1 | 0 | 1 |  
| 2 | 0 | 0 | 1 | 0 | 

Suddenly, we notice that if we can store the result in a array that can store all the bits in every bit position that exactly appears %3 == 1 (e.g, 1, 4, 7 ...) times. Then we find what we want. (in this case, [0, 1, 0, 1] == 5)

This works with any cases, e.g. [6, 1, 3, 3, 3, 6, 6],
| Num / Bit | 3 | 2 | 1 | 0 |
| ---- | :-:| :-: | :-: | :-: |
| 6 | 0 | 1 | 1 | 0 | 
| 1 | 0 | 0 | 0 | 1 | 
| 3 | 0 | 0 | 1 | 1 | 
| 3 | 0 | 0 | 1 | 1 | 
| 3 | 0 | 0 | 1 | 1 | 
| 6 | 0 | 1 | 1 | 0 | 
| 6 | 0 | 1 | 1 | 0 | 

So the bit that appears exactly  %3 == 1 (e.g, 1, 4, 7 ...) times is the "1" at position 0 (4 times), which is [0, 0, 0, 1] == 1

Then, how can we achive this?

Think about what we learned from AND, OR, XOR operants.

- AND == 1 when bits of a and b are exactly SAME and have True values.

- OR == 1 when bits of a and b are at least one have a True value

- XOR == 1 when bits of a and b are exactly OPPOSITE (e.g 0x10b XOR 0x01b == 0x11b)

Notice something, right? If a bit appears once, its OR operation result will be 1. if it appears twice, its AND operation result will be also 1. What about three times? Well, if it reached three-time appearance, we want to remove (or 'reset') this bit, using XOR.

We use variable 'once' and 'twice' to store the pervious state of bits in all position. Initially, they are all zeros. Also, we implement a bit mask to filter out bits that occurs every three times. Lets back to case [2, 2, 5, 2] to see how the algorithm works when triversing [2, 2, 5, 2]:
1. bin(2) == 0x0010, once = once ^ bin(2) = 0x0010 (Note: 0 XOR any non-zero value equals that value)
2. bin(2) == 0x0010, twice = twice | ( once & bin(2) ) = 0x0010, once = once ^ bin(2) = 0x0000
3. bin(5) == 0x0101, twice = twice | ( once & bin(5) ) = 0x0010, once = once ^ bin(5) = 0x0101

Before we enter the final step of the triversing loop, let's recall the purpose of the mask first. It is used to filter out the duplicated bits and remain the bit that shown exactly once. So, firstly, if a bit had shown twice, it will be the 1 in relating positions in once and twice.

4. bin(2) == 0x0010, twice = twice = twice | ( once & bin(2) ) = 0x0010, once = once ^ bin(2) = 0x0111
   
   - If we check the common bits in once and twice, using twice & once, we get 0x0010, which is exactly the number 2 we want to exclude
   - To exclude, it, we can do a inverse operation, ~(twice & once) = 0x1101. This is the mask we want
   - To apply this mask, we simply do:
        ```
        once &= mask
        twice &= mask
        ```
        This remove the bits that appears eactly three times at current stage

Finally, we get the result __5__ we want. In O(n) time and O(1) space.
