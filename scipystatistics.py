"""
scipy_stats_natural_gas.py
========================================
This script is designed for students.

It demonstrates how to:
    - Load a CSV file with natural gas data (naturalgasbyzip.csv)
    - Use pandas to inspect and prepare the data
    - Use SciPy to compute a variety of statistics:
        * Descriptive statistics (mean, median, std, skew, kurtosis, etc.)
        * Confidence interval for the mean
        * Normality tests
        * Correlations
        * Hypothesis tests (t-test between groups)
        * Simple linear regression

The script uses:
    - Error handling (try/except) so it doesn't crash on common problems
    - Copious comments explaining each step

REQUIREMENTS:
    - Python 3.x
    - pandas
    - scipy
    - numpy (usually installed automatically with SciPy)
    - This uses the data from https://www.kaggle.com/datasets/alexandrepetit881234/natural-gas-consumption-by-zip-code
"""

# ---------------------------
# 1. IMPORT LIBRARIES
# ---------------------------

# We wrap imports in try/except so that if a library is missing,
# the script doesn't crash with a confusing error message.
try:
    import pandas as pd
    import numpy as np
except ImportError as e:
    print("ERROR: Could not import pandas or numpy.")
    print("Make sure you have installed them, e.g.:")
    print("    pip install pandas numpy")
    raise e  # Re-raise so the student sees the actual error too

try:
    from scipy import stats
except ImportError as e:
    print("ERROR: Could not import SciPy.")
    print("Make sure you have installed it, e.g.:")
    print("    pip install scipy")
    raise e


# ---------------------------
# 2. CONFIGURATION
# ---------------------------

# Name of the CSV file to load.
# Make sure this file is in the same directory as the script,
# or provide a full/relative path.
CSV_PATH = "naturalgasbyzip.csv"

# Preferred column for detailed analysis.
# If this column does not exist, we will fall back to the first numeric column.
PREFERRED_NUMERIC_COLUMN = "Consumption (therms)"

# Optional categorical column to try group comparisons (for t-tests)
POSSIBLE_GROUP_COLUMN = "Building type"


# ---------------------------
# 3. HELPER FUNCTIONS
# ---------------------------

def load_data(csv_path):
    """
    Load the CSV file using pandas.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded DataFrame.

    Raises:
        FileNotFoundError: If the file cannot be found.
        pd.errors.EmptyDataError: If the file is empty.
        Exception: Any other unexpected error is re-raised.
    """
    try:
        df = pd.read_csv(csv_path)
        print(f"Successfully loaded data from: {csv_path}")
        return df
    except FileNotFoundError as e:
        print(f"ERROR: File not found: {csv_path}")
        print("Check that the file name and path are correct.")
        raise e
    except pd.errors.EmptyDataError as e:
        print(f"ERROR: File is empty: {csv_path}")
        raise e
    except Exception as e:
        print("ERROR: An unexpected error occurred while loading the data.")
        raise e


def choose_numeric_column(df, preferred_name=None):
    """
    Choose a numeric column for detailed analysis.

    Args:
        df (pd.DataFrame): The DataFrame.
        preferred_name (str or None): Name of a preferred column.

    Returns:
        str: The name of the chosen numeric column.

    Raises:
        ValueError: If no numeric columns are found.
    """
    # Select only numeric columns (int, float, etc.)
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if not numeric_cols:
        raise ValueError("No numeric columns found in the dataset.")

    if preferred_name is not None and preferred_name in numeric_cols:
        print(f"Using preferred numeric column: {preferred_name}")
        return preferred_name

    # Fallback: use the first numeric column
    chosen = numeric_cols[0]
    print(f"Preferred column not found. Using first numeric column instead: {chosen}")
    return chosen


# ---------------------------
# 4. MAIN ANALYSIS FUNCTION
# ---------------------------

def analyze_data(df):
    """
    Perform a wide range of statistics using SciPy on the given DataFrame.

    Args:
        df (pd.DataFrame): The loaded data.
    """
    print("\n==================== BASIC DATA INFO ====================")
    # Show the first few rows for context (students can see what columns exist)
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    print("\nDataFrame info():")
    df.info()

    # Show numeric columns
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    print("\nNumeric columns detected:")
    print(numeric_cols)

    if not numeric_cols:
        print("No numeric columns available for statistical analysis. Exiting.")
        return

    # Choose a main numeric column for detailed analysis
    try:
        target_col = choose_numeric_column(df, PREFERRED_NUMERIC_COLUMN)
    except ValueError as e:
        print("ERROR:", e)
        return

    # Drop missing values from the target column to avoid NaN issues
    # (Many SciPy functions can't handle NaNs)
    series = df[target_col].dropna()

    print(f"\n==================== DESCRIPTIVE STATS for '{target_col}' ====================")
    # Basic descriptive stats using pandas (for convenience)
    desc = series.describe()
    print(desc)

    # Additional SciPy-based descriptive stats
    # (These are similar to pandas, but we show SciPy usage explicitly.)
    data = series.values  # Convert to NumPy array for SciPy

    try:
        mean_val = np.mean(data)
        median_val = np.median(data)
        std_val = np.std(data, ddof=1)  # sample std dev (ddof=1)
        skew_val = stats.skew(data, bias=False)
        kurtosis_val = stats.kurtosis(data, bias=False)  # Fisher's definition (0 = normal)
    except Exception as e:
        print("ERROR computing basic statistics with SciPy:", e)
        return

    print(f"\nMean (SciPy/NumPy): {mean_val:.4f}")
    print(f"Median (SciPy/NumPy): {median_val:.4f}")
    print(f"Standard Deviation (sample, SciPy/NumPy): {std_val:.4f}")
    print(f"Skewness (SciPy): {skew_val:.4f}")
    print(f"Kurtosis (SciPy, Fisher=0 for normal): {kurtosis_val:.4f}")

    # ---------------------------
    # 4.1 Confidence Interval for the Mean
    # ---------------------------
    print(f"\n==================== CONFIDENCE INTERVAL (Mean of '{target_col}') ====================")
    try:
        # We compute a 95% confidence interval using the t-distribution.
        # stats.sem = standard error of the mean.
        confidence_level = 0.95
        n = len(data)
        mean = np.mean(data)
        sem = stats.sem(data)

        # Degrees of freedom for t-distribution
        dfree = n - 1

        # t critical value
        t_crit = stats.t.ppf((1 + confidence_level) / 2, df=dfree)

        # margin of error
        moe = t_crit * sem

        ci_lower = mean - moe
        ci_upper = mean + moe

        print(f"Sample size: {n}")
        print(f"Mean: {mean:.4f}")
        print(f"Standard error of the mean (SEM): {sem:.4f}")
        print(f"{int(confidence_level * 100)}% CI: ({ci_lower:.4f}, {ci_upper:.4f})")
    except Exception as e:
        print("ERROR computing confidence interval:", e)

    # ---------------------------
    # 4.2 Normality Test
    # ---------------------------
    print(f"\n==================== NORMALITY TEST for '{target_col}' ====================")
    print("Using SciPy's normaltest (D’Agostino and Pearson’s test):")
    try:
        # normaltest requires at least 8 observations
        if len(data) >= 8:
            k2, p_value = stats.normaltest(data)
            print(f"Statistic: {k2:.4f}, p-value: {p_value:.4g}")
            if p_value < 0.05:
                print("Result: Data is likely NOT normal (reject H0 at α=0.05).")
            else:
                print("Result: Cannot reject normality (data may be normal).")
        else:
            print("Not enough data points for normaltest (need at least 8).")
    except Exception as e:
        print("ERROR performing normality test:", e)

    # ---------------------------
    # 4.3 Correlation Between Two Numeric Columns
    # ---------------------------
    print("\n==================== CORRELATION ANALYSIS ====================")
    # If we have at least two numeric columns, try computing correlation
    if len(numeric_cols) >= 2:
        # Choose second numeric column for correlation (different from target_col)
        other_numeric = [col for col in numeric_cols if col != target_col]
        if other_numeric:
            col2 = other_numeric[0]
            print(f"Computing correlation between '{target_col}' and '{col2}'")

            # Drop NaNs for both columns at the same time
            pair_df = df[[target_col, col2]].dropna()
            x = pair_df[target_col].values
            y = pair_df[col2].values

            try:
                # Pearson correlation (linear relationship)
                pearson_r, pearson_p = stats.pearsonr(x, y)
                print(f"Pearson correlation: r = {pearson_r:.4f}, p-value = {pearson_p:.4g}")

                # Spearman correlation (monotonic relationship)
                spearman_rho, spearman_p = stats.spearmanr(x, y)
                print(f"Spearman correlation: ρ = {spearman_rho:.4f}, p-value = {spearman_p:.4g}")
            except Exception as e:
                print("ERROR computing correlation:", e)
        else:
            print("Only one numeric column available; skipping correlation.")
    else:
        print("Fewer than two numeric columns; skipping correlation.")

    # ---------------------------
    # 4.4 Group Comparison with t-test (if a categorical column exists)
    # ---------------------------
    print("\n==================== GROUP COMPARISON (t-test) ====================")
    if POSSIBLE_GROUP_COLUMN in df.columns:
        print(f"Attempting t-test on '{target_col}' grouped by '{POSSIBLE_GROUP_COLUMN}'")
        group_col = POSSIBLE_GROUP_COLUMN

        # Drop rows where either the numeric or group column is missing
        gdf = df[[target_col, group_col]].dropna()

        # Find the unique groups (categories)
        groups = gdf[group_col].unique()

        if len(groups) < 2:
            print(f"Not enough groups in '{group_col}' for a t-test (found {len(groups)} group(s)).")
        else:
            # For simplicity, we will only compare the first two groups
            g1, g2 = groups[:2]
            print(f"Comparing groups: '{g1}' vs '{g2}'")

            data_g1 = gdf[gdf[group_col] == g1][target_col].values
            data_g2 = gdf[gdf[group_col] == g2][target_col].values

            try:
                t_stat, p_val = stats.ttest_ind(data_g1, data_g2, equal_var=False)  # Welch's t-test
                print(f"t-statistic: {t_stat:.4f}, p-value: {p_val:.4g}")
                if p_val < 0.05:
                    print("Result: Significant difference between groups at α=0.05.")
                else:
                    print("Result: No significant difference between groups at α=0.05.")
            except Exception as e:
                print("ERROR performing t-test:", e)
    else:
        print(f"Column '{POSSIBLE_GROUP_COLUMN}' not found; skipping group comparison.")

    # ---------------------------
    # 4.5 Simple Linear Regression (SciPy)
    # ---------------------------
    print("\n==================== SIMPLE LINEAR REGRESSION ====================")
    # We can reuse the same pair of numeric columns from correlation, if available.
    if len(numeric_cols) >= 2:
        other_numeric = [col for col in numeric_cols if col != target_col]
        if other_numeric:
            col2 = other_numeric[0]
            print(f"Performing linear regression: '{target_col}' (y) ~ '{col2}' (x)")

            reg_df = df[[target_col, col2]].dropna()
            x = reg_df[col2].values
            y = reg_df[target_col].values

            try:
                # SciPy's simple linear regression
                slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

                print(f"Slope: {slope:.4f}")
                print(f"Intercept: {intercept:.4f}")
                print(f"R-squared (coefficient of determination): {r_value ** 2:.4f}")
                print(f"p-value for slope: {p_value:.4g}")
                print(f"Standard error of slope: {std_err:.4f}")
            except Exception as e:
                print("ERROR performing linear regression:", e)
        else:
            print("Only one numeric column available; skipping linear regression.")
    else:
        print("Fewer than two numeric columns; skipping linear regression.")

    print("\n==================== ANALYSIS COMPLETE ====================")


# ---------------------------
# 5. MAIN ENTRY POINT
# ---------------------------

def main():
    """
    Main function that:
        1. Loads the data.
        2. Runs the SciPy-based statistical analysis.
    """
    try:
        df = load_data(CSV_PATH)
    except Exception:
        # If loading fails, we stop the script here
        print("Failed to load data. Exiting.")
        return

    # Run our analysis on the loaded DataFrame
    analyze_data(df)


if __name__ == "__main__":
    main()
