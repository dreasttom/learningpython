"""
demo_seaborn.py

A teaching script that demonstrates how to use the seaborn
package for data visualization in Python.

This script:
- Imports seaborn safely with error handling
- Creates a sample dataset using pandas and numpy
- Shows how to make:
    * scatter plot with regression line
    * bar plot
    * box plot
    * heatmap (correlation matrix)
- Uses detailed comments so students can follow along
"""

# -----------------------------
# IMPORTS WITH ERROR HANDLING
# -----------------------------
try:
    import seaborn as sns
except ImportError as e:
    # If seaborn is not installed, provide a clear message and exit
    raise SystemExit(
        "Error: The 'seaborn' package is not installed.\n"
        "Install it by running:\n"
        "    pip install seaborn\n"
        "and then run this script again."
    ) from e

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_sample_data():
    """
    Create a small sample dataset to visualize.

    Returns:
        pd.DataFrame: A DataFrame with numeric and categorical data.
    """
    # Set a seed so results are reproducible (students will see same numbers each run)
    np.random.seed(42)

    # Create 100 fake "students"
    n = 100

    # Example features: exam scores, study hours, and class (A/B/C)
    math_scores = np.random.normal(loc=75, scale=10, size=n)      # average ~75
    reading_scores = np.random.normal(loc=70, scale=12, size=n)   # average ~70
    study_hours = np.random.uniform(low=0, high=10, size=n)       # between 0 and 10 hours
    classes = np.random.choice(['A', 'B', 'C'], size=n)           # class labels

    # Build a DataFrame
    df = pd.DataFrame({
        'MathScore': math_scores,
        'ReadingScore': reading_scores,
        'StudyHours': study_hours,
        'Class': classes
    })

    return df


def plot_scatter_with_regression(df):
    """
    Make a scatter plot with a regression line using seaborn's regplot.

    Args:
        df (pd.DataFrame): DataFrame with 'StudyHours' and 'MathScore' columns.
    """
    try:
        # Basic input validation
        required_columns = {'StudyHours', 'MathScore'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise ValueError(f"Missing required columns for scatter plot: {missing}")

        plt.figure(figsize=(8, 6))  # control the figure size

        # regplot creates a scatter + regression line
        sns.regplot(
            data=df,
            x='StudyHours',
            y='MathScore',
            ci=95,          # 95% confidence interval around regression line
            scatter_kws={'alpha': 0.6},  # transparency for points
            line_kws={'linewidth': 2}    # thicker regression line
        )

        plt.title("Study Hours vs Math Score (with regression line)")
        plt.xlabel("Study Hours")
        plt.ylabel("Math Score")
        plt.tight_layout()
        plt.show()

    except ValueError as ve:
        print(f"[plot_scatter_with_regression] ValueError: {ve}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"[plot_scatter_with_regression] Unexpected error: {e}")


def plot_categorical_bar(df):
    """
    Make a bar plot showing average MathScore per Class.

    Args:
        df (pd.DataFrame): DataFrame with 'MathScore' and 'Class' columns.
    """
    try:
        required_columns = {'MathScore', 'Class'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise ValueError(f"Missing required columns for bar plot: {missing}")

        plt.figure(figsize=(8, 6))

        # barplot automatically computes and shows the mean of the numeric variable
        sns.barplot(
            data=df,
            x='Class',
            y='MathScore',
            errorbar='sd'  # show standard deviation as error bars
        )

        plt.title("Average Math Score by Class")
        plt.xlabel("Class")
        plt.ylabel("Average Math Score")
        plt.tight_layout()
        plt.show()

    except ValueError as ve:
        print(f"[plot_categorical_bar] ValueError: {ve}")
    except Exception as e:
        print(f"[plot_categorical_bar] Unexpected error: {e}")


def plot_boxplot(df):
    """
    Make a box plot of MathScore grouped by Class.

    Args:
        df (pd.DataFrame): DataFrame with 'MathScore' and 'Class' columns.
    """
    try:
        required_columns = {'MathScore', 'Class'}
        if not required_columns.issubset(df.columns):
            missing = required_columns - set(df.columns)
            raise ValueError(f"Missing required columns for box plot: {missing}")

        plt.figure(figsize=(8, 6))

        # boxplot is useful to show distribution, median, and potential outliers
        sns.boxplot(
            data=df,
            x='Class',
            y='MathScore'
        )

        plt.title("Distribution of Math Scores by Class (Box Plot)")
        plt.xlabel("Class")
        plt.ylabel("Math Score")
        plt.tight_layout()
        plt.show()

    except ValueError as ve:
        print(f"[plot_boxplot] ValueError: {ve}")
    except Exception as e:
        print(f"[plot_boxplot] Unexpected error: {e}")


def plot_correlation_heatmap(df):
    """
    Make a heatmap of the correlation matrix of numeric columns.

    Args:
        df (pd.DataFrame): DataFrame with numeric columns.
    """
    try:
        # Select only numeric columns (heatmap doesn't work well with strings)
        numeric_df = df.select_dtypes(include=[np.number])

        if numeric_df.shape[1] == 0:
            raise ValueError("No numeric columns available for correlation heatmap.")

        # Compute correlation matrix
        corr = numeric_df.corr()

        plt.figure(figsize=(8, 6))

        # heatmap visualizes the correlation matrix
        sns.heatmap(
            corr,
            annot=True,        # show correlation values inside the squares
            fmt=".2f",         # format for the numbers (2 decimal places)
            cmap="coolwarm",   # color map for better contrast
            square=True
        )

        plt.title("Correlation Heatmap of Numeric Features")
        plt.tight_layout()
        plt.show()

    except ValueError as ve:
        print(f"[plot_correlation_heatmap] ValueError: {ve}")
    except Exception as e:
        print(f"[plot_correlation_heatmap] Unexpected error: {e}")


def main():
    """
    Main function to run all the plots.

    This is where:
    - The sample data is created.
    - Each plotting function is called.
    """
    # Create our sample dataset
    df = create_sample_data()

    # Optional: quick look at the data
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Set a nice Seaborn style for all plots
    sns.set_theme(style="whitegrid")

    # Call each plotting function
    plot_scatter_with_regression(df)
    plot_categorical_bar(df)
    plot_boxplot(df)
    plot_correlation_heatmap(df)


if __name__ == "__main__":
    # Only run main() if this file is executed directly
    # (Not when imported as a module)
    main()
