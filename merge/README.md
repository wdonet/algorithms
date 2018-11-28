# Merge Sort

Divide the original array until have one element and then start merging every subarray

- Time complexity: O(n log n)
- Space complexity: O(n log n)
- Recursive
- Divide and conquer

# Algorithm

1. If there is one or zero elements, it's already sorted, otherwise
2. Divide the array in two arrays of same length
3. Sort each array
4. Merge both arrays

## Steps

Sort: 2, 4, 1, 6, 8, 5, 3, 7

### 1. Divide in two arrays:

        2,4,1,6,8,5,3,7
         /          \
        /            \
    L=2,4,1,6     R=8,5,3,7
     
    
### 2. Sort L & R

    1,2,4,6     3,5,7,8
    
### 3. Merge L & R

    1,2,4,6     3,5,7,8
        \         /
         \       /
      1,2,3,4,5,6,7,8
   
## Merge Process

Find the smallest element which has not being processed from two arrays
        
     1,2,4,6   3,5,7,8   compares: 1<3? finalArray = 1 
         4,6   3,5,7,8   compares: 2<3? finalArray = 1,2
         4,6   3,5,7,8   compares: 4<3? finalArray = 1,2,3
         4,6     5,7,8   compares: 4<5? finalArray = 1,2,3,4
           6     5,7,8   compares: 6<5? finalArray = 1,2,3,4,5
           6       7,8   compares: 6<7? finalArray = 1,2,3,4,5,6
                   7,8   compares: 6<7? finalArray = 1,2,3,4,5,6
                   
When one array is empty, we only need to add the missing elements to the finalArray

    finalArray = 1,2,3,4,5,6,7,8
     
    
## How to sort L & R

Keep dividing the array until have only one element

            2,4,1,6,8,5,3,7
             /           \
       2,4,1,6           8,5,3,7
        /    \          /      \
      2,4    1,6       8,5    3,7
      / \    / \       / \    /  \
     2  4   1   6     8  5   3    7
     
Then apply the merge process to every sub-array

            1,2,3,4,5,6,7,8
             /         \
       1,2,4,6        3,5,7,8
        /    \        /     \
      2,4    1,6     5,8    3,7
      / \    / \     / \   /  \
     2  4   1  6    8  5  3    7
    
# Pseudocode
```
    mergeSort(A) is
        n ← length(A)
        if (n >= 2) then
            mid ← n/2
            L ← A[0 … mid-1]
            R ← A[mid … n]
            mergeSort(L)
            mergeSort(R)
            merge(L, R, A)
        end if
    end
    
    merge (L, R, A) is
        nL ← length(L)
        nR ← length(R)
        i ← j ← k ← 0
        while (i < nL && j < nR) do
            if (L[i] <= R[j]) then
                A[k] ← L[i] 
                i ← i + 1
            else
                A[k] ← R[j]
                j ← j + 1
            end if
            k ← k + 1
        end while
        while (i < nL) do
            A[k] ← L[i] 
            i ← i + 1
            k ← k + 1
        end while
        while (j < nR) do
            A[k] ← R[j]
            j ← j + 1
            k ← k + 1
        end while
    end
```

# Functionality
![mergeSortGif](Merge-sort.gif)

