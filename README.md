
Task 1:

Project Title & Logo

Flight management system

Description:

For my Flight Management System project, I developed four modules. Each module has applied different OOP concept such as aggregation, polymorphism and abstraction. It stores the flights/ International flight, passengers, and airline related details with encapsulation. The passenger stores all passenger details and the flight store its flight information like origin and destination. The airline.py allow user add or remove flight from the system and store its related information. The airline class’s core function is to represent an airline name and managing a list of flights. The International_flight class is similar with the flight class, which it used to store the International flight information.

The system helps to simplify airline data management and provide a modular structure for handling passengers and flights. It helps user easily adding passenger information into the data system.

Installation instructions:

The program require install PyQt5 with inputting "pip install PyQt5" in the terminal.

Usage:

Run the main.py file and filled with requried information (e.g Passenger name, Passenger number, Age, Gender, flight type). Then the user could click the "Add Passenger" button to update passenger information.

Flight added with domestic flight:
<img width="310" height="193" alt="image" src="https://github.com/user-attachments/assets/5ff07132-d01f-4f31-bea5-d42f3e1f8322" />
Flight added with International flight:
<img width="297" height="192" alt="image" src="https://github.com/user-attachments/assets/c7ab96d9-a01a-46f7-a063-6475e6f777a1" />


Features

Built with GUI: Flight management system have the GUI and allow the user to add new passenger information. Passenger Management: The program allow user add new passenger for the flight. The passenger information will store until the passenger number reached the maximum number.


Task 2:

Description:

I selected the heap as my data structure and heap sort as my algorithm. The min-heap helps the program efficiently manage and retrieve data, while heap sort provides effective data retrieval with optimal time complexity and minimal memory usage.

Abstract Data Type (ADT) Definition
Abstract Data Type (ADT) is a conceptual model. They define what a data structure does without dictating how it does it. 

Heap could be min-heap or max heap. For the min-heap, it is a complete binary tree. The value of the root node must be the smallest among all its descendant nodes and the same thing must be done for its left and right sub-tree(parent ≤ children). Max heap is a binary tree data structure where the parent node is always greater than or equal to its children, ensuring the largest element at the root. The time complexity of largest element in the max-heap or smallest element in the min heap is the O(1). The difference between min-heap and max-heap is min-heap’s minimum key element present at the root while the max-heap’s maximum key element present at the root. A min-heap uses the ascending priority and max-heap uses the descending priority. 

There are some common operation on a Heap Data Structure:

Insertion:

In the insertion, the inserted value added into the end of list of heap. Then calculate the child index number and use the child in the heap list compare with parent nodes. The code is implementing the min heap, where if the parent is larger than child. The parent node and child node needed to be switched. After that, the new index will become number to retrieve the parent node and continue the while loop for comparison.  

For example, I began with a list of values and inserted them sequentially into the heap array using the insertion procedure. For example, I have a list [31, 41, 51, 100]. When I insert a new number 13, the array looks like [31, 41, 51, 100, 13] before the swap executed. The parent of 13 is 41, which is larger than the child 13 and a swap occurs. The new list becomes [31, 13, 51, 100, 41]. Because 13 is still smaller than its new parent 31. The swaps will be executed and the new result is [13, 31, 51, 100, 41]. If there’s another element 16 inserted. The list is [13, 31, 51, 100, 41, 16]. The 51 is the parent node of 16, and it is larger than child node. It needed to swaps and the list becomes [13, 31, 16, 100, 41, 51]. In this structure, 31 and 16 are children of 13; 100 and 41 are children of 31; and 51 is the child of 16.

Application:

Heap:

min-heap is used to implement priority queues, where the smallest element is always retrieve first. Heap Sort:

Heap sort is used on largest dataset handling, where the memory usage could be minimized.
