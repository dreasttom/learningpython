"""
Sorting Data in Python
----------------------
This script demonstrates how to sort:
    1. A list of numbers
    2. A list of dictionaries (e.g., student records)
    3. A pandas DataFrame

It includes error handling and student-friendly comments.
"""

# -------- IMPORTS --------
import pandas as pd


# ----------- Example 1: Sorting a List -----------

def sort_list(numbers):
    """
    Takes a list of numbers and returns it sorted in ascending and descending order.
    Includes error handling if the input cannot be converted to floats.
    """

    try:
        # Try converting all values to float
        nums = [float(x) for x in numbers]
        
        ascending = sorted(nums)
        descending = sorted(nums, reverse=True)

        return ascending, descending

    except ValueError:
        raise ValueError("All values must be numbers.")


# ----------- Example 2: Sorting a List of Dictionaries -----------

def sort_students_by_key(students, key_name):
    """
    Sorts a list of dictionaries based on a given dictionary key.

    Example student structure:
        students = [
            {"name": "Alice", "score": 85},
            {"name": "Bob", "score": 92},
        ]
    """

    try:
        return sorted(students, key=lambda x: x[key_name])

    except KeyError:
        raise KeyError(f"Key '{key_name}' does not exist in dictionary items.")


# ----------- Example 3: Sorting a pandas DataFrame -----------

def sort_dataframe(df, column_name, ascending=True):
    """
    Sorts a pandas DataFrame by a column.

    Parameters:
        df          → pandas DataFrame
        column_name → column to sort by
        ascending   → True = ascending, False = descending
    """

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")

    return df.sort_values(by=column_name, ascending=ascending)


# ----------- MAIN TEST CODE -----------

if __name__ == "__main__":
    
    print("==== Example 1: Sorting a List ====")
    demo_numbers = ["10", "5", "2.5", "30"]
    asc, desc = sort_list(demo_numbers)
    print("Original:", demo_numbers)
    print("Ascending:", asc)
    print("Descending:", desc)
    print()

    print("==== Example 2: Sorting a List of Dictionaries ====")
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78}
    ]
    sorted_students = sort_students_by_key(students, "score")
    print("Sorted by score:", sorted_students)
    print()

    print("==== Example 3: Sorting a DataFrame ====")
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Score": [85, 92, 78]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    df_sorted = sort_dataframe(df, "Score", ascending=False)
    print("\nSorted by score (descending):\n", df_sorted)
