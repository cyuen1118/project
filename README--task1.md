# project
Task 1:


Project Title & Logo

Flight management system

Description:

This project provide the three module for better managing the flight information. The passenger stores all passenger details, the flight store information like origin and destination. The airline.py allow user add or remove flight from the system. The system helps to simplify airline data management and provide a modular structure for handling passengers and flights. It helps user adding passenger information into the data system.

Installation instructions:

The program require install PyQt5 with inputting "pip install PyQt5" in the terminal.

Usage:

Run the main.py file and filled with requried information (e.g Passenger name, Passenger number, Age, Gender). Then the user could click the "Add Passenger" button to update passenger information.

Features

Built with GUI: Flight management system have the GUI and allow the user to add new passenger information. Passenger Management: The program allow user add new passenger for the flight. The passenger information will store until the passenger number reached the maximum number.



Task 2:


Description:

I selected the heap as my data structure and heap sort as my algorithm. The min-heap helps the program efficiently manage and retrieve data, while heap sort provides effective data retrieval with optimal time complexity and minimal memory usage.

Abstract Data Type (ADT) Definition

Heap could be min-heap or max heap. For the min-heap, it is a complete binary tree. The value of the root node must be the smallest among all its descendant nodes and the same thing must be done for its left and right sub-tree(parent ≤ children).

There are some common operation on a Heap Data Structure:

Insertion:

Add the new element to the end of the heap, in the next available position in the last level of the tree.
Compare the new element with its parent. If the parent is greater than the new element, swap them.
repeat step 2 until the parent is smaller than or equal to the new element,or until the new element reaches the root of the tree.
Deletion:

Replace the root with the last element in the heap
Remove the last element from the heap, since it has been moved to the root.
Heap-down: The element now at the root may violate the Min-Heap property, so perform heapify starting from the root to restore the heap property.
For the heap sort, it is a comparison-based sorting algorithm based on the Binary Heap data structure. The algorithm repeatedly finds the maximum (or minimum) element and swaps it with the last (or first) element. To execute the heap sort, the algorithm will first visualize the array as a complete binary tree. Then it will build a Max Heap and sort the array by placing largest element at end of unsorted array.

Application:

Heap:

min-heap is used to implement priority queues, where the smallest element is always retrieve first.
Heap Sort:

Heap sort is used on largest dataset handling, where the memory usage could be minimized.
