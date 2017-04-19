# Bubble Sort

Compares every element i the list with the following element, changing the elements if they are in a wrong sort

It's necessary to review the list several times until no  changes are needed.

- Time complexity: θ(n^2)
- Space complexity: θ(n)

## Algorithm

```
begin BubbleSort(list)
   for all elements of list
      if list[i] > list[i+1]
         swap(list[i], list[i+1])
      end if
   end for 
   return list
end BubbleSort
```

## Step by step

Sort: 5, 1, 4, 2, 8

First pass:

__5 1__ 4 2 8 -> __1 5__ 4 2 8
    

## Functionality

![insertionSortGif](Bubble-sort-.gif)

