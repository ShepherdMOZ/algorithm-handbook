
## Question

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

## Analysis

This is equivalent to find out the all sub sets of a given set. It is a __Combination__ type question. 

A pair of nested loop can solve the problem. The first loop enumerate elements in the source set, the second loop concatenate the element from first loop to all previous generated powersets.