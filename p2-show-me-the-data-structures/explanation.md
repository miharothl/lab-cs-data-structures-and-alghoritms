# Project 2: Show Me the Data Structures


## Problem 1: LRU Cache

To efficiently solve the LRU cache, I use a combination of Queue and Map (dictionary).

The queue is used to track the order of the `use_operations` (get and set). The size of the queue is the size of LRU
cache capacity. The queue is implemented using the python list. The time complexity of the items' enqueuing and dequeuing has a time complexity of O(1).

The Map is used as the lookup table. For a given key, it will return the value of the document. To prevent map size growth indefinitely,
items that are least recently used items dequeued from the queue are removed. The time complexity of map operations like
setting, getting, and removing the key-value pairs has a time complexity of O(1).

The overall time and space efficiency of the implemented LRU cache are of O(1).

## Problem 2: File Recursion

To solve file recursion, I used a recursion algorithm implemented in `find_files_recursive`. A file system is a Tree data structure.
The recursive function recursively enters a directory and stores results of files that we are looking for `suffix`
into python list `found_files = []`. I used append operation to add the results to the list, which has a time complexity
of O(1).

The overall time and space efficiency of the implemented solution is O(n), where n is the number of files and directories
that need to be visited.

## Problem 3: Huffman Coding

The solution to the Huffman Coding problem involved using the Map, Priority Queue, and Binary Tree.

The `Huffman` class has to static methods `encode` and `decode`. Encoding of the data consists of three steps:

1. count character frequencies `__count_frequency`
2. build a Huffman Tree and `__build_tree`
3. encode the data

I used Map to count the character frequencies. Get and set operation on Map have time complexity of O(1); however, I have to traverse the data in a loop with time complexity O(n). The space complexity of this operation is also O(n).

I enqueued counted data frequencies in the priority queue. I used python implementation, which internally uses a binary heap `heapq`
with time complexity O(log N) for push and same for pop operation. Items with low occurrence will dequeue first.

To build a Huffman Tree, I used a Binary Tree. For the unbalanced binary tree, insert operation has a time complexity of O(n); however, in this case
the Tree is balanced, and I would assume O(log n) time complexity.

Finally, I need to encode the data. I used a loop to visit each character and then searched for the minimal encoding weight by
searching the Hofman Tree with time complexity O(log n). So the overall encoding time complexity is O(n log n).

Decoding is very similar to encoding and the overall time complexity of the algorithm is O(n log n), overall space complexity is O(n)

## Problem 4: Active Directory

Active directory problem is similar to Problem 2. Active directory is a Tree data structure. I used a recursive algorithm implemented in `is_user_in_group`
to traverse the Tree and to find if a user is in a group. As we don't know if the Tree is balanced, I'm assuming the worst-case scenario where
the time complexity of finding the user in a group is O(n).

## Problem 5: BlockChain

To solve the BlockChain, I used a Linked List, tracking both head and tail, allowing constant insert complexity O(1).
Space complexity is O(n).

## Problem 6: Union and Intersection

The Union of the two Linked Lists' solution involved using a Map to find the frequency of the elements in both lists first. I needed to loop through the linked lists
(O(n)) and set items to the Map (O(1)). To populate the Union Linked List I implemented the `insert` method that inserts elements at constant time O(1).

Solving the Intersection involved one additional step. I needed to transform each linked list into a Set by using Map. After that 
I was able to calculate the Intersection by using another Map as a frequency counter.

The overall time and space complexity of the implemented algorithm is O(n).