# Bubble Sort
Compares every element in the list with the following element, changing the elements if they are in a wrong sort.

It's necessary to review the list several times until no  changes are needed, which indicates the list is sorted

- Time complexity:
  - Best: O(n)
  - Average: O(n^2)
- Space complexity: In Place

## Step by step
Sort: 5, 1, 4, 2, 8

First pass:
- __5 1__ 4 2 8 -> __1 5__ 4 2 8 - swap(5,1)
- 1 __5 4__ 2 8 -> 1 __4 5__ 2 8 - swap(5,4)
- 1 4 __5 2__ 8 -> 1 4 __2 5__ 8 - swap(5,2)
- 1 4 2 __5 8__ -> 1 4 2 __5 8__

Second pass:
- __1 4__ 2 5 8 -> __1 4__ 2 5 8
- 1 __4 2__ 5 8 -> 1 __2 4__ 5 8 - swap(4,2)
- 1 2 __4 5__ 8 -> 1 2 __4 5__ 8
- 1 2 4 __5 8__ -> 1 2 4 __5 8__

Third pass:
- __1 2__ 4 5 8 -> __1 2__ 4 5 8
- 1 __2 4__ 5 8 -> 1 __2 4__ 5 8
- 1 2 __4 5__ 8 -> 1 2 __4 5__ 8
- 1 2 4 __5 8__ -> 1 2 4 __5 8__

Since no more changes the list is sorted

## Pseudocode
```
do
  swapped = false
  for i = 1 to indexOfLastUnsortedElement
    if leftElement > rightElement
      swap(leftElement, rightElement)
      swapped = true
while swapped
```


## Functionality
![insertionSortGif](Bubble-sort-.gif)

