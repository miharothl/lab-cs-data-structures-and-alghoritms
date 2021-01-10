# Project 3: Problems vs. Algorithms

## Problem 1: Sqrt of Integer

To efficiently Sqrt of Integer is used a variation of Binary Search.

The time complexity of the algorithm is O(log(n)), and space complexity is O(1).

## Problem 2: Search in Rotated Sorted Array

Like the first problem, I used Binary Search to find a solution for the Search in Rotated Sorted Array problem.

The time complexity of the algorithm is O(log(n)), and space complexity is O(1).

## Problem 3: Rearrange Digits

To solve the Rearange Digits, the array has to be sorted first. The requirement was that the problem
is solved in time complexity O(log(n)) without built-in sort algorithms.

I decided to implement QuickSort first, which has a time complexity O(n log(n)) and space complexity
O(log(n)).

Once I was able to sort the array using QuickSort, I used the loop to build the two numbers to maximum their sum.

## Problem 4: Dutch National Flag

This problem is similar to Sort012, where the input array of 0, 1, and 2 has to be sorted in a single traversal.
The idea is to place all the 0s on the left and all the 2s on the right side of the array, which automatically solves 1s.

The time complexity of the algorithm is O(n), space complexity O(1).

## Problem 5: Autocomplete with Tries

As suggested, we had to use the Trie data structure to complete the Autocomplete problem. Trie is using the Map data
structure to implement the tree of nodes which support find and insert operations.

Time complexity is O(n) to load the data structure where n is the number of words and O(k) to find the suffixes where k is the number of words that share the same prefix.

## Problem 6: Min Max of Un-Sorted Array

I traversed the array by keeping the min and max values.

The time complexity of the algorithm is O(n) and space complexity O(1).

## Problem 7: HTTP Router with Tries

Similarly to the Autocomplete problem, I used the Trie algorithm to implement an HTTP router.

Time complexity is O(n) to load the data structure, where n is the number of handlers and is O(k) to find the handler, where k I number of path suffixes.

