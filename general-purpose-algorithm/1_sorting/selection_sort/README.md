## Selection Sort
Time Complexity: Avg.O(n^2) Best.O(n^2) Worst.O(n^2)

Stability: Unstable

### Design

Repeat the following steps:
1. scan the whole array
2. find the min/max number
3. move the number to the begin/end of the array by swapping the first/last element with the min/max value
4. set the begin of scan to the first position of unsorted part of the array


Until the array is in-order