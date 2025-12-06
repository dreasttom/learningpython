"""
numpy_demo_for_students.py

This script demonstrates many important NumPy features,
with *copious comments* designed to teach students the
logic behind array creation, manipulation, and computation.

Topics covered:
    1. Array Creation
    2. Array Shapes and Reshaping
    3. Indexing, Slicing, Boolean Masking
    4. Broadcasting
    5. Mathematical Functions (ufuncs)
    6. Aggregation (sum, mean, etc.)
    7. Linear Algebra
    8. Random Number Generation
    9. Stacking and Splitting
"""

import numpy as np


# ============================================================
# 1. ARRAY CREATION
# ============================================================

print("\n=== 1. ARRAY CREATION ===\n")

# Create a simple 1D array from a Python list
a1 = np.array([1, 2, 3, 4])
print("1D array a1:", a1)

# Create a 2D array (matrix) from a list of lists
a2 = np.array([[1, 2, 3],
               [4, 5, 6]])
print("\n2D array a2:\n", a2)

# Arrays of zeros
z = np.zeros((3, 4))
print("\nZeros array (3x4):\n", z)

# Arrays of ones
o = np.ones((2, 5))
print("\nOnes array (2x5):\n", o)

# Range of numbers (like Python's range but returns an array)
r = np.arange(0, 10, 2)   # Start at 0, stop before 10, step 2
print("\nRange array np.arange(0,10,2):", r)

# Linearly spaced numbers between 0 and 1
lin = np.linspace(0, 1, 5)
print("\nLinearly spaced array from 0 to 1:", lin)

# Identity matrix (square matrix with 1s on diagonal)
I = np.eye(4)
print("\nIdentity matrix:\n", I)


# ============================================================
# 2. ARRAY SHAPES AND RESHAPING
# ============================================================

print("\n=== 2. ARRAY SHAPES AND RESHAPING ===\n")

# Shape of an array
print("Shape of a2:", a2.shape)

# Reshape a 1D array into 2D
reshaped = np.arange(12).reshape((3, 4))
print("\nReshaped array (3x4):\n", reshaped)

# Flatten array into 1D view
flat = reshaped.ravel()
print("\nFlattened version of reshaped:", flat)

# Transpose (swap axes)
print("\nTranspose of a2:\n", a2.T)


# ============================================================
# 3. INDEXING, SLICING, BOOLEAN MASKING
# ============================================================

print("\n=== 3. INDEXING, SLICING, BOOLEAN MASKING ===\n")

# 1D indexing
print("Third element of a1:", a1[2])   # zero‐based index

# 2D indexing
print("Element at row=1, col=2 of a2:", a2[1, 2])

# Slicing (start:stop)
print("\na1[1:3] =", a1[1:3])

# Slicing rows and columns
print("\na2 first row:", a2[0, :])
print("a2 second column:", a2[:, 1])

# Boolean masking
print("\na1:", a1)
mask = a1 > 2
print("Mask (a1 > 2):", mask)
print("Filtered values:", a1[mask])


# ============================================================
# 4. BROADCASTING
# ============================================================

print("\n=== 4. BROADCASTING ===\n")

# Broadcasting allows operations between arrays of different shapes.

A = np.ones((3, 3))
b = np.array([1, 2, 3])

# NumPy automatically "stretches" b to match A's shape
print("A:\n", A)
print("b:", b)
print("\nA + b (broadcasting b across rows):\n", A + b)


# ============================================================
# 5. MATH FUNCTIONS (UFUNCS)
# ============================================================

print("\n=== 5. MATH FUNCTIONS (UFUNCS) ===\n")

x = np.linspace(0, np.pi, 5)
print("x values:", x)
print("sin(x):", np.sin(x))
print("cos(x):", np.cos(x))
print("exp(x):", np.exp(x))

# Elementwise operations
print("\nx**2 =", x**2)
print("sqrt(x) =", np.sqrt(x))


# ============================================================
# 6. AGGREGATION FUNCTIONS
# ============================================================

print("\n=== 6. AGGREGATION FUNCTIONS ===\n")

M = np.arange(1, 10).reshape((3, 3))
print("Matrix M:\n", M)

print("Sum of all elements:", np.sum(M))
print("Column-wise sum:", np.sum(M, axis=0))
print("Row-wise sum:", np.sum(M, axis=1))

print("Mean of M:", np.mean(M))
print("Max of M:", np.max(M))
print("Min of M:", np.min(M))


# ============================================================
# 7. LINEAR ALGEBRA
# ============================================================

print("\n=== 7. LINEAR ALGEBRA ===\n")

A = np.array([[2, 1],
              [1, 3]])
b = np.array([1, 2])

print("Matrix A:\n", A)
print("Vector b:", b)

# Solve Ax = b
x = np.linalg.solve(A, b)
print("\nSolution to Ax = b:", x)

# Determinant
print("det(A):", np.linalg.det(A))

# Matrix multiplication
print("\nA @ A:\n", A @ A)


# ============================================================
# 8. RANDOM NUMBER GENERATION
# ============================================================

print("\n=== 8. RANDOM NUMBER GENERATION ===\n")

rng = np.random.default_rng()

print("Random numbers (uniform 0-1):", rng.random(5))
print("Random normal distribution:", rng.normal(0, 1, 5))
print("Random integers 0–10:", rng.integers(0, 10, 5))


# ============================================================
# 9. STACKING AND SPLITTING
# ============================================================

print("\n=== 9. STACKING AND SPLITTING ===\n")

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Vertical stack (rows on top of each other)
vstacked = np.vstack((A, B))
print("Vertical stack:\n", vstacked)

# Horizontal stack (columns side-by-side)
hstacked = np.hstack((A, B))
print("\nHorizontal stack:\n", hstacked)

# Splitting arrays
split_example = np.arange(10)
print("\nSplit example array:", split_example)
print("Split into 2 parts:", np.split(split_example, 2))


print("\n=== END OF NUMPY DEMO ===")
