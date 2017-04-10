#### [<- Go Back](/) ####

## Heap sort

Given a disordered list of elements, the _Heap Sort Algorithm_ goal is to rearrange those elements in natural order.

For instance,

 - Input: [6, 8, 12, 11, 15, 13, 20, 3, 10]
 - Output: [3, 6, 8, 10, 11, 12, 13, 15, 20]

A **heap** is a _binary tree_ where:

1) each node is greater than each of its children
2) the tree is perfectly balanced
3) all leaves are in the left most position available.

### Time Complexity:

 - Best **O(nlog(n))**
 - Average **O(nlog(n))**
 - Worst **O(nlog(n))**

### Solution

Heap sort happens in two phases.
 - **Phase I**
    - The array is transformed into a heap. 

![creatingTheHeap](http://i.imgur.com/qCn3Gj3.gifv)
[link](https://cl.ly/383L0O3i1h29)

 - **Phase II**
    - The heap is continuously reduced to a sorted array, while the heap is not empty
        - Remove the top of the head into an array
        - Fix the heap.

![sortingTheHeap](http://i.imgur.com/uVuQuY7.gifv)
[link](https://cl.ly/3o2P1e123N3q)

#### Reference
 - http://btv.melezinek.cz/binary-heap.html
