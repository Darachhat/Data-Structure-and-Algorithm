## What are Data Structures and Algorithms?

- **Data Structures** (រចនាសម្ព័ន្ធទិន្នន័យ):  
  The way data is organized, stored, and managed in memory so it can be used efficiently.  
  **Khmer:** Data structures គឺជារបៀបដែលយើងរក្សាទុកទិន្នន័យក្នុងរបៀបផ្សេងៗ។

  **Example:**  
  - **Array:** Stores data in a consecutive block of memory.  
    ```python
    arr = [1, 2, 3, 4, 5]
    ```
  - **Linked List:** Each element points to the next, allowing for efficient insertions/removals.

- **Algorithms** (ក្បួនដោះស្រាយបញ្ហា):  
  A step-by-step procedure or formula for solving a problem, often manipulating or searching data in data structures.  
  **Khmer:** Algorithms គឺជារបៀបដែលយើងដោះស្រាយបញ្ហា ភាគច្រើនប្រើក្នុងការស្វែងរក និងការរៀបចំ data structures។

  **Example:**  
  - **Searching:** Finding an item in an array.  
  - **Sorting:** Arranging numbers from low to high.

---

## Key Concepts

### 1. Time Complexity 
A measure of how long an algorithm takes to run as input size grows.
- **Khmer:** Time complexity គឺជារង្វាស់នៃរយៈពេលដែល Algorithm ត្រូវការដើម្បីដោះស្រាយបញ្ហា។  
- **Example:**  
  - Linear Search: O(n), checks each element once.

### 2. Space Complexity 
A measure of how much extra memory an algorithm uses.
- **Khmer:** Space complexity គឺជារង្វាស់នៃ memory ដែល Algorithm បានប្រើ។  
- **Example:**  
  - An algorithm that uses a new array of size n has O(n) space complexity.

### 3. Big O Notation 
A mathematical notation to describe the upper bound of an algorithm's running time or space requirements as the input size grows.
- **Khmer:** Big O Notation គឺជា សញ្ញាណគណិតវិទ្យាដែលបង្ហាញអំពីដែនកំណត់នៃអនុគមន៍។  
- **Example:**  
  - Bubble Sort: O(n²)  
  - Binary Search: O(log n)

### 4. Recursion
A programming technique where a function calls itself to solve smaller subproblems.
- **Khmer:** Recursion គឺជាបច្ចេកទេស programming នៅពេលដែល functions ហៅខ្លួនឯងមកប្រើ។  
- **Example:**  
  ```python
  def factorial(n):
      if n == 0:
          return 1
      return n * factorial(n - 1)
  ```

### 5. Divide and Conquer
A strategy to solve complex problems by breaking them down into smaller, simpler subproblems, solving each recursively, and combining the results.
- **Khmer:** Divide និង Conquer គឺជាវិធីសាស្រ្តក្នុងការដោះស្រាយបញ្ហាដោយបំបែកវាទៅជាផ្នែកតូចៗ លធ្វើអោយយើងងាយស្រួលគ្រប់គ្រងនិង ដោះស្រាយបញ្ហា និង Recursion ត្រូវបានហើយប្រើប្រាស់ជាញឹកញាប់នៅពេលដែលប្រើប្រាស់វិធីសាស្រ្តមួយនេះក្នុង Algorithm 
- **Example:**  
  - Merge Sort, Quick Sort

### 6. Brute Force (ល្បិចសាមញ្ញ)
A straightforward approach that tries all possible solutions and picks the best one.
- **Khmer:** Brute Force គឺជាវិធីសាមញ្ញមួយ ដោយ algorithms ធ្វើការសាកល្តងគ្រប់ដំណោះស្រាយទាំងអស់ដែលអាចទៅរួច បន្ទាប់មកជ្រើសរើសជម្រើសល្អបំផុតមកប្រើ
- **Example:**  
  - Checking every possible password combination.

---

## Sorting Algorithms Examples

### Bubble Sort

- **Description:**  
  Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- **Khmer:** Bubble sort គឺជា algorithm ដែលតម្រៀបតម្លៃក្នុង array ពីទាបទៅខ្ពស់។
- **Example in Python:**
  ```python
  def bubble_sort(arr):
      n = len(arr)
      for i in range(n):
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
      return arr

  print(bubble_sort([5, 2, 9, 1, 5]))
  # Output: [1, 2, 5, 5, 9]
  ```

### Selection Sort

- **Description:**  
  Finds the smallest element in the unsorted part and moves it to the front.
- **Khmer:** Selection sort គឺជា algorithm ដែលស្វែងរកតម្លៃទាបបំផុតក្នុង array រួចផ្លាស់ទីវាមកមុខ។
- **Example in Python:**
  ```python
  def selection_sort(arr):
      n = len(arr)
      for i in range(n):
          min_idx = i
          for j in range(i+1, n):
              if arr[j] < arr[min_idx]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
      return arr

  print(selection_sort([5, 2, 9, 1, 5]))
  # Output: [1, 2, 5, 5, 9]
  ```

---

## Summary Table

| Concept             | Khmer Translation                                             | Example / Note                     |
|---------------------|--------------------------------------------------------------|------------------------------------|
| Data Structure      | រចនាសម្ព័ន្ធទិន្នន័យ                                        | Array, Linked List                 |
| Algorithm           | ក្បួនដោះស្រាយបញ្ហា                                          | Searching, Sorting                 |
| Time Complexity     | រយៈពេល                                                     | O(n), O(n²)                        |
| Space Complexity    | ការប្រើប្រាស់ memory                                         | O(1), O(n)                         |
| Big O Notation      | សញ្ញា Big O                                                 | O(n), O(log n)                     |
| Recursion           | ការហៅខ្លួនឯង                                               | Function calls itself              |
| Divide & Conquer    | បំបែក និងជោគជ័យ                                            | Merge Sort, Quick Sort             |
| Brute Force         | ល្បិចសាមញ្ញ                                                 | Trying all combinations            |
| Bubble Sort         | ការតម្រៀបដោយបំបែកកន្លែងជាប់គ្នា                            | Repeatedly swap adjacent elements  |
| Selection Sort      | ការតម្រៀបដោយជ្រើសរើសតម្លៃតូចបំផុត                        | Select min and move to front       |

---﻿# Data-Structure-and-Algorithm
