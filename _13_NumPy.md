# NumPy _____ Python Library

A simple guide to learn NumPy step by step, in easy English, with examples.

---

## 1. What is NumPy?

NumPy is a Python library used to work with **numbers and lists of numbers** (called arrays) in a fast and easy way.

Think of it like a super-powered list. A normal Python list can hold numbers, but it is slow for math. NumPy arrays are made for math and are much faster.

```python
import numpy as np
```

We always give it the short name `np` so we don't have to type `numpy` every time.

---

## 2. Install NumPy

```bash
pip install numpy
```

---

## 3. What is an Array?

An array is just a list of numbers, but the NumPy version.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
# [1 2 3 4]
```

The big difference from a normal Python list: you can do math directly on it.

```python
list1 = [1, 2, 3]
# list1 * 2  -> this would repeat the list, NOT multiply each number

arr1 = np.array([1, 2, 3])
print(arr1 * 2)
# [2 4 6]   <- multiplies every number
```

---

## 4. 1D and 2D Arrays

**1D array** = a simple line of numbers (like one row).

```python
a = np.array([1, 2, 3])
```

**2D array** = numbers arranged in rows and columns (like a table).

```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])
```

You can check how many rows and columns it has:

```python
print(b.shape)   # (2, 3) -> 2 rows, 3 columns
```

---

## 5. Useful Ways to Create Arrays

```python
np.zeros((2, 3))     # array full of 0
np.ones((2, 3))      # array full of 1
np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]  (like Python's range)
np.linspace(0, 1, 5) # 5 numbers evenly spaced between 0 and 1
```

---

## 6. Checking Array Information

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)   # (2, 3)  -> rows and columns
print(arr.ndim)    # 2       -> how many dimensions
print(arr.size)    # 6       -> total numbers inside
print(arr.dtype)   # int64   -> type of numbers stored
```

---

## 7. Getting Items (Indexing)

Same as Python lists, but with rows and columns for 2D.

```python
arr = np.array([10, 20, 30, 40])
print(arr[0])    # 10 (first item)
print(arr[-1])   # 40 (last item)
```

For a 2D array, you tell it the row and the column:

```python
matrix = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(matrix[0, 0])  # 1  -> row 0, column 0
print(matrix[1, 2])  # 6  -> row 1, column 2
print(matrix[0])     # [1 2 3]  -> whole first row
print(matrix[:, 1])  # [2 5]    -> whole column 1
```

---

## 8. Slicing (Taking a Part of the Array)

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])   # [20 30 40]   -> from index 1 to 3
print(arr[:3])    # [10 20 30]   -> first 3 items
print(arr[::-1])  # [50 40 30 20 10]  -> reversed
```

**Good to know:** If you slice an array and then change a value, it can also change the original array. If you don't want that, use `.copy()`:

```python
part = arr[0:2].copy()
```

---

## 9. Changing the Shape (Reshape)

You can rearrange numbers into a new shape, as long as the total count matches.

```python
arr = np.arange(6)          # [0 1 2 3 4 5]
new = arr.reshape(2, 3)     # 2 rows, 3 columns
print(new)
# [[0 1 2]
#  [3 4 5]]
```

---

## 10. Doing Math on Arrays

This is the best part of NumPy — you don't need loops.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [4 10 18]
print(a / b)   # [0.25 0.4 0.5]
print(a ** 2)  # [1 4 9]
```

You can also do math with a single number (this is called **broadcasting** — it just means NumPy applies it to every item):

```python
print(a + 10)   # [11 12 13]
print(a * 2)    # [2 4 6]
```

---

## 11. Comparing Numbers

```python
a = np.array([1, 2, 3, 4, 5])
print(a > 3)
# [False False False True True]
```

You can use this to **filter** numbers:

```python
print(a[a > 3])
# [4 5]
```

This means: "give me only the numbers bigger than 3." Very useful for real data.

---

## 12. Common Math Functions

```python
arr = np.array([1, 2, 3, 4, 5])

print(arr.sum())    # 15   -> total
print(arr.mean())   # 3.0  -> average
print(arr.min())    # 1    -> smallest
print(arr.max())    # 5    -> largest
print(np.sqrt(arr)) # square root of each number
```

For 2D arrays, you can choose to work by row or column using `axis`:

```python
matrix = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(matrix.sum(axis=0))  # [5 7 9]   -> add each column
print(matrix.sum(axis=1))  # [6 15]    -> add each row
```

Simple way to remember: `axis=0` goes **down** (column-wise), `axis=1` goes **across** (row-wise).

---

## 13. Sorting

```python
arr = np.array([3, 1, 4, 1, 5])
print(np.sort(arr))
# [1 1 3 4 5]
```

---

## 14. Joining Arrays

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate([a, b]))
# [1 2 3 4 5 6]
```

---

## 15. Random Numbers

```python
np.random.seed(1)             # makes random numbers repeat the same way every time (good for testing)

print(np.random.rand(3))            # 3 random decimal numbers between 0 and 1
print(np.random.randint(1, 10, 5))  # 5 random whole numbers between 1 and 9
```

---

## 16. A Small Practice Example

Let's say you have test scores and want simple stats:

```python
scores = np.array([78, 85, 90, 45, 67, 88, 92, 55])

print("Average score:", scores.mean())
print("Highest score:", scores.max())
print("Lowest score:", scores.min())
print("Passing scores (>=50):", scores[scores >= 50])
```

Output:
```
Average score: 75.0
Highest score: 92
Lowest score: 45
Passing scores (>=50): [78 85 90 67 88 92 55]
```

---

## Quick Cheat Sheet

| What you want to do | Code |
|---|---|
| Make an array | `np.array([1,2,3])` |
| Array of zeros | `np.zeros((2,3))` |
| Array of ones | `np.ones((2,3))` |
| Range of numbers | `np.arange(0,10,2)` |
| Shape of array | `arr.shape` |
| Get one item | `arr[0]` |
| Get a row (2D) | `matrix[0]` |
| Get a column (2D) | `matrix[:, 0]` |
| Slice part of array | `arr[1:4]` |
| Change shape | `arr.reshape(2,3)` |
| Add/multiply arrays | `a + b`, `a * b` |
| Filter numbers | `arr[arr > 5]` |
| Sum/average | `arr.sum()`, `arr.mean()` |
| Sort | `np.sort(arr)` |
| Join arrays | `np.concatenate([a,b])` |
| Random numbers | `np.random.rand(3)` |

---

## What to Practice Next

1. Create a few arrays and print `.shape`, `.ndim`, `.size` until it feels natural.
2. Practice slicing 1D and 2D arrays.
3. Try math operations (`+`, `-`, `*`, `/`) between two arrays.
4. Try filtering with conditions like `arr[arr > 10]`.
5. Use `sum()`, `mean()`, `max()`, `min()` on some fake data (like scores or prices).

Once these feel easy, you're ready to move to more advanced NumPy topics (broadcasting rules, linear algebra, performance tricks) or start learning **Pandas**, which uses NumPy underneath.