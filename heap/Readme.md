#### [<- Go Back](https://github.com/wdonet/algorithms) ####

# Heap sort

Given a disordered list of elements, the _Heap Sort Algorithm_ goal is to rearrange those elements in natural order.

For instance,

 - Input: [6, 8, 12, 11, 15, 13, 20, 3, 10]
 - Output: [3, 6, 8, 10, 11, 12, 13, 15, 20]

A **heap** is a _binary tree_ where:

1) each node is greater than each of its children
2) the tree is perfectly balanced
3) all leaves are in the left most position available.

## Notes

### Indexes

  - **Left** Child  = 2 * _i_ + 1
  - **Right** Child = 2 * _i_ + 2
  
  where _i_ is the parent's index
   
 ![indexes](http://i.imgur.com/bp1FFjF.png)

### Time Complexity:

 - Best **O(nlog(n))**
 - Average **O(nlog(n))**
 - Worst **O(nlog(n))**

### Solution

Heap sort happens in two phases.
 - **Phase I**
    - The array is transformed into a heap. 

![creatingTheHeap](https://d3vv6lp55qjaqc.cloudfront.net/items/3S23250G3T2r002n1m1o/Screen%20Recording%202017-04-10%20at%2003.46%20AM.gif)
[link](https://cl.ly/383L0O3i1h29)

 - **Phase II**
    - The heap is continuously reduced to a sorted array, while the heap is not empty
        - Remove the top of the head into an array
        - Fix the heap.

![sortingTheHeap](https://d3vv6lp55qjaqc.cloudfront.net/items/423f3M410x080H161M05/Screen%20Recording%202017-04-10%20at%2003.52%20AM.gif)
[link](https://cl.ly/3o2P1e123N3q)

#### Tools of Reference
 - http://btv.melezinek.cz/binary-heap.html
