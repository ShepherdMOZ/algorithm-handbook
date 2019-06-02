### Analysis

To do this in O(n^2) is simple. You just need another array to save the sum of all pairs of two digits, starting from 1st and 2nd, untill (n-1)th and nth. Then we scan the sum array when new sum is added, to check if anything inside these sums equals k, 

But we want to get the bonus, which means doing this in linear time constrain O(n). So, we want a new data structure to store sums that we can access to any values instantly, without scanning the whole array. That is the Hashmap

Luckily, both Python and Java provide built-in class to do this.