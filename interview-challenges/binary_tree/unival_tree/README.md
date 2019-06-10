## Question

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

They are:
```
1 * 3 (the three bottom child node without any further child) ; 
0 (the only child node without any child); 
and
   1
  / \
 1   1
```