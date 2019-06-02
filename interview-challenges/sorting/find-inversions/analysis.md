## Analysis

To do this in O(n^2), or quadratic time constrain, is quite simple, it is just a similar apporach to the bubble sort. However, if we want to get the outcome quicker, we need to find some non-linear structure to store and proceed the data.

You might start thinking, "Well, does any sorting algorithm help to solve the issue". Definetely! As I mentioned earlier, the quadratic time solution is based on bubble sort. And if we want to do something faster, like in quasilinear time... Wait! Is the description of question mentioned something I saw somewhere else before? "Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j...". 

Aha, merge sort!

The O(nlogn) solution for the question is exactly based on a tiny clever modification on the classic merge sort algorithm. Let's just quickly recall this algorithm. To get [2,4,1,3,5] -> [1,2,3,4,5], the merge sort will

1. Divide the array in two parts recursively, until there is only one element left in each child node
    ```
       [2,4,1,3,5]
         /     \
      [2,4] [1,3,5]
      /  \    /  \
    [2] [4] [1] [3,5]
                /   \
              [3]   [5]
    ```
2. Merge two array. If the array itself is in order, the left side is expect to have smaller integers than right side. So we always append left side's element first unless a integer in the right side is smaller than the left side. In this example, when we merge [2,4] and [1,3,5]
    
    (1) 1 is smaller than 2,4, so we append 1 first

    (2) 3 is larger than 2, so we append 2

    (3) 3 is smllar than 4, so we append 3

    (4) Moving on, the remaining part can already be appended in predetermined order

The rule in 2 is applied to this code:
```
        while i < len(left) and j < len(right) :
            if left[i] <= right[j]:
                ### Normal order
                merged.append(left[i])
                i += 1
            else:
                ### Inverted order
                merged.append(right[j])
                j += 1
```

Now we find that, if we can add something to store the state in the "Inverted order" part of code, we find our answer.

And that is:
```
            else:
                ### Inverted order
                for number in left[i:]:
                    inverted.append((number,right[j]))
                merged.append(right[j])
                j += 1
```

Hey, before you move to the next question, think about this question. Why:
```
for number in left[i:]:
    nverted.append((number,right[j]))
``` 
is able to give us all the inverted parts against right[j] in the array?