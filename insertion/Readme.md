#### [<- Go Back](https://github.com/wdonet/algorithms) ####

# Insertion sort

This algorithm sorts the array of elements one item at a time.  It is not efficient for a large list of elements.

Advantages:

- Simple to implement
- More efficient for small list of elements and partially sorted lists
- Efficient for the use of memory, it only requires O(1) of additional memory space

## Procedure

1. Loop over positions in the array, starting with index = 1 (_not 0 when the array is zero-based_). That index contains the **pivot**.
2. Start temporal index (**j**) to index-1
3. While j >= 0 Do
  + Compare pivot vs content at j
  + if it is greater, _move content to the right_ from j to j+1
  + Decrease j in 1
4. Set pivot content at j+1 _(once j has reached the beginning of the array or the right place in the sorted elements at left side)_

The pivot is the content at any new position hold separately, and you need to insert it into the correct place at the sorted sub-array to the left of that position.

The algorithm could start from the right or from the left (which is more common).  The process is similar but opposite in the comparison and the direction of the movement of elements. 

![insertionSortGif](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)

## Time Complexity:

 - Best **O(n)** _(when it is already sorted)_
 - Average **O(n^2)**
 - Worst **O(n^2)**
 
#### Tools of Reference

- 
- Test at [insertionSortTest.py](test/insertionSortTest.py)
