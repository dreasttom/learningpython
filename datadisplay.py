"""
student_chart_gui_with_dataframe.py
====================================

This script demonstrates:

1. Creating synthetic (made-up) data.
2. Storing that data in pandas DataFrames.
3. Visualizing the data with matplotlib using:
       - Bar chart
       - Line chart
       - Pie chart
       - Histogram
       - Scatter plot
       - Box plot
4. Providing a simple GUI (Graphical User Interface) using tkinter
   so the user can select which chart to display.
5. Using basic error handling (try/except) to avoid crashes.

Intended for students learning:
- Python
- pandas
- matplotlib
- tkinter
"""

# ----------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------

import random

import pandas as pd                   # For DataFrame
import matplotlib.pyplot as plt       # For plotting

import tkinter as tk                  # Standard GUI library for Python
from tkinter import ttk, messagebox   # ttk for nicer widgets, messagebox for dialogs


# ----------------------------------------------------------
# DATA CREATION
# ----------------------------------------------------------

def create_sample_data():
    """
    Create synthetic data and return it as pandas DataFrames.

    Returns:
        df_sales (pd.DataFrame): Contains Month and Sales columns.
        df_random (pd.DataFrame): Contains random numeric values.
        df_scatter (pd.DataFrame): Contains X and Y columns for scatter plot.
        product_names (list of str): Labels for pie chart.
        product_shares (list of float): Percentages for pie chart.
    """

    # Fake sales data for 6 months
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [150, 200, 180, 220, 210, 260]

    # Build a DataFrame for monthly sales
    df_sales = pd.DataFrame({
        "Month": months,
        "Sales": sales
    })

    # Random values (e.g., test scores, measurements, etc.) for histogram/box plot
    random_values = [random.randint(50, 150) for _ in range(60)]
    df_random = pd.DataFrame({
        "Value": random_values
    })

    # Data for scatter plot: X vs. Y with a roughly linear relationship + noise
    x_values = list(range(1, 21))
    y_values = [x * 3 + random.randint(-10, 10) for x in x_values]
    df_scatter = pd.DataFrame({
        "X": x_values,
        "Y": y_values
    })

    # Pie chart data: product names and their share of total sales (in %)
    product_names = ["Product A", "Product B", "Product C", "Product D"]
    product_shares = [40, 25, 20, 15]  # Should sum to ~100

    return df_sales, df_random, df_scatter, product_names, product_shares


# ----------------------------------------------------------
# PLOTTING FUNCTIONS (EACH CHART GETS ITS OWN FUNCTION)
# ----------------------------------------------------------

def plot_bar_chart(df_sales):
    """
    Plot a bar chart of Sales vs. Month using df_sales DataFrame.
    """
    try:
        # Basic validation
        if "Month" not in df_sales.columns or "Sales" not in df_sales.columns:
            raise KeyError("df_sales must contain 'Month' and 'Sales' columns.")

        plt.figure(figsize=(8, 5))
        plt.bar(df_sales["Month"], df_sales["Sales"])

        plt.xlabel("Month")
        plt.ylabel("Sales (units)")
        plt.title("Monthly Sales - Bar Chart")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Bar Chart Error", f"Error while plotting bar chart:\n{e}")


def plot_line_chart(df_sales):
    """
    Plot a line chart of Sales vs. Month using df_sales DataFrame.
    """
    try:
        if "Month" not in df_sales.columns or "Sales" not in df_sales.columns:
            raise KeyError("df_sales must contain 'Month' and 'Sales' columns.")

        plt.figure(figsize=(8, 5))
        plt.plot(df_sales["Month"], df_sales["Sales"], marker="o")

        plt.xlabel("Month")
        plt.ylabel("Sales (units)")
        plt.title("Monthly Sales - Line Chart")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Line Chart Error", f"Error while plotting line chart:\n{e}")


def plot_pie_chart(product_names, product_shares):
    """
    Plot a pie chart of product sales share.
    """
    try:
        if len(product_names) != len(product_shares):
            raise ValueError("product_names and product_shares must have the same length.")

        total_share = sum(product_shares)
        if not (99.5 <= total_share <= 100.5):
            # Not critical, but let the user know
            messagebox.showwarning(
                "Pie Chart Warning",
                f"Product shares do not sum to ~100 (total={total_share}). "
                "The chart will still be plotted."
            )

        plt.figure(figsize=(6, 6))
        plt.pie(product_shares, labels=product_names, autopct="%1.1f%%")
        plt.title("Product Sales Share - Pie Chart")
        plt.axis("equal")  # Make the pie a circle
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Pie Chart Error", f"Error while plotting pie chart:\n{e}")


def plot_histogram(df_random):
    """
    Plot a histogram of values using df_random DataFrame.
    """
    try:
        if "Value" not in df_random.columns:
            raise KeyError("df_random must contain a 'Value' column.")

        plt.figure(figsize=(8, 5))
        plt.hist(df_random["Value"], bins=10, edgecolor="black")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.title("Histogram of Random Values")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Histogram Error", f"Error while plotting histogram:\n{e}")


def plot_scatter(df_scatter):
    """
    Plot a scatter plot using df_scatter DataFrame (X vs. Y).
    """
    try:
        if "X" not in df_scatter.columns or "Y" not in df_scatter.columns:
            raise KeyError("df_scatter must contain 'X' and 'Y' columns.")

        plt.figure(figsize=(8, 5))
        plt.scatter(df_scatter["X"], df_scatter["Y"])

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Scatter Plot Example")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Scatter Plot Error", f"Error while plotting scatter plot:\n{e}")


def plot_box_plot(df_random):
    """
    Plot a box plot using df_random DataFrame.
    """
    try:
        if "Value" not in df_random.columns:
            raise KeyError("df_random must contain a 'Value' column.")

        plt.figure(figsize=(6, 5))
        plt.boxplot(df_random["Value"], patch_artist=True)
        plt.title("Box Plot of Random Values")
        plt.ylabel("Value")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Box Plot Error", f"Error while plotting box plot:\n{e}")


# ----------------------------------------------------------
# GUI: BUILDING A SIMPLE TKINTER INTERFACE
# ----------------------------------------------------------

def build_gui(df_sales, df_random, df_scatter, product_names, product_shares):
    """
    Build and run a tkinter GUI that lets the user select which chart to plot.

    Args:
        df_sales, df_random, df_scatter: pandas DataFrames for different charts.
        product_names, product_shares: Data for pie chart.
    """

    # Callback function for when the user clicks the "Plot" button
    def on_plot_button_click():
        """
        Determine which chart type is selected and call the corresponding
        plotting function.
        """
        chart = chart_type_var.get()  # Get the selected value from the dropdown

        if chart == "Bar Chart":
            plot_bar_chart(df_sales)
        elif chart == "Line Chart":
            plot_line_chart(df_sales)
        elif chart == "Pie Chart":
            plot_pie_chart(product_names, product_shares)
        elif chart == "Histogram":
            plot_histogram(df_random)
        elif chart == "Scatter Plot":
            plot_scatter(df_scatter)
        elif chart == "Box Plot":
            plot_box_plot(df_random)
        else:
            # This should not happen if we set up the options correctly
            messagebox.showerror("Selection Error", "Unknown chart type selected.")

    # Try to create the main window
    try:
        root = tk.Tk()
    except Exception as e:
        print("Error creating Tkinter root window:", e)
        return

    root.title("Student Chart Viewer")

    # Optional: Set a minimum size for the window
    root.minsize(400, 200)

    # Create a frame to hold the widgets (for better layout control)
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Label at the top
    label = ttk.Label(main_frame, text="Select a chart type to display:")
    label.pack(pady=10)

    # Dropdown (combobox) for chart selection
    chart_type_var = tk.StringVar(value="Bar Chart")  # Default value

    chart_types = [
        "Bar Chart",
        "Line Chart",
        "Pie Chart",
        "Histogram",
        "Scatter Plot",
        "Box Plot"
    ]

    chart_combo = ttk.Combobox(
        main_frame,
        textvariable=chart_type_var,
        values=chart_types,
        state="readonly"  # User cannot type arbitrary text
    )
    chart_combo.pack(pady=5)

    # Plot button
    plot_button = ttk.Button(
        main_frame,
        text="Plot Selected Chart",
        command=on_plot_button_click
    )
    plot_button.pack(pady=20)

    # Information label at the bottom
    info_label = ttk.Label(
        main_frame,
        text="Close the chart window to return to this menu."
    )
    info_label.pack(pady=5)

    # Start the Tkinter event loop (this keeps the window open)
    root.mainloop()


# ----------------------------------------------------------
# MAIN FUNCTION
# ----------------------------------------------------------

def main():
    """
    Main entry point of the script.
    1. Creates DataFrames with synthetic data.
    2. Builds and runs the GUI.
    """
    try:
        df_sales, df_random, df_scatter, product_names, product_shares = create_sample_data()
    except Exception as e:
        print("Error creating sample data:", e)
        return

    # (Optional) Print DataFrames to console so students can see them
    print("Sales DataFrame:\n", df_sales, "\n")
    print("Random Values DataFrame:\n", df_random.head(), "...\n")
    print("Scatter DataFrame:\n", df_scatter.head(), "...\n")

    # Build and start the GUI
    build_gui(df_sales, df_random, df_scatter, product_names, product_shares)


# ----------------------------------------------------------
# RUN SCRIPT
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
