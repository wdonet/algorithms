# Selection sort

* Time complexity: θ(n^2)
* Space complexity: θ(n)
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

## Reference

http://www.algolist.net/Algorithms/Sorting/Selection_sort