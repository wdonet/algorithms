# Selection sort

* Time complexity: θ(n^2)
* Space complexity: In place
* Very simple implementation

## Algorithm

### Preconditions

* Divide the input into two parts: Sublist of items already sorted and the sublist of items remaining
to be sorted
* Initially the list of sorted items is empty and the unsorted list is the whole list
* The sorted list will be built from the left to the right of the input list

1. Let i be the index of the last element in the sorted list (which initially will be zero)
2. Find the lowest element in the unsorted list (which initially is the whole list)
3. Add the element found to the sorted list, which means, swap the found element with the element in index i
4. Increase i and repeat from step 2  

## Comparision vs other O(n^2) sort algorithms

* It improves bubble sort by making only one exchange for every pass through the list

## Example

Worst case iterations:<br/>
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]<br/>
[1, 9, 8, 7, 6, 5, 4, 3, 2, 10]<br/>
[1, 2, 8, 7, 6, 5, 4, 3, 9, 10]<br/>
[1, 2, 3, 7, 6, 5, 4, 8, 9, 10]<br/>
[1, 2, 3, 4, 6, 5, 7, 8, 9, 10]<br/>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br/>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br/>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br/>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br/>
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]<br/>

Best case iterations:<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br/>

Average case iterations:<br/>
[4, 9, 8, 0, 5, 8, 6, 7, 5, 8]<br/>
[0, 9, 8, 4, 5, 8, 6, 7, 5, 8]<br/>
[0, 4, 8, 9, 5, 8, 6, 7, 5, 8]<br/>
[0, 4, 5, 9, 8, 8, 6, 7, 5, 8]<br/>
[0, 4, 5, 5, 8, 8, 6, 7, 9, 8]<br/>
[0, 4, 5, 5, 6, 8, 8, 7, 9, 8]<br/>
[0, 4, 5, 5, 6, 7, 8, 8, 9, 8]<br/>
[0, 4, 5, 5, 6, 7, 8, 8, 9, 8]<br/>
[0, 4, 5, 5, 6, 7, 8, 8, 9, 8]<br/>
[0, 4, 5, 5, 6, 7, 8, 8, 8, 9]<br/>


## Reference

http://www.algolist.net/Algorithms/Sorting/Selection_sort