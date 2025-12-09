"""
Grouped Bar Graph with Tkinter GUI and pandas
---------------------------------------------
This script shows how to:

    * Build a simple GUI using Tkinter
    * Read user input (subject names + comma-separated scores)
    * Store the data in a pandas DataFrame
    * Create a grouped (side-by-side) bar chart using matplotlib
    * Include error handling and student-friendly comments

Run this file with Python (e.g., python grouped_gui_pandas.py).
"""

# ---------- IMPORTS ----------
import tkinter as tk                  # Tkinter for the GUI
from tkinter import messagebox        # Pop-up error/info dialogs

import pandas as pd                   # pandas for data handling
import numpy as np                    # numpy for numerical operations

import matplotlib.pyplot as plt       # matplotlib for plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# FigureCanvasTkAgg lets us show matplotlib graphs inside Tkinter


# ---------- HELPER FUNCTIONS ----------

def parse_scores(text):
    """
    Convert a comma-separated string into a list of floats.

    Example:
        "10, 12.5, 9" --> [10.0, 12.5, 9.0]

    If something goes wrong, this function raises ValueError
    with a student-friendly error message.
    """
    text = text.strip()

    if not text:
        raise ValueError("You must enter at least one score.")

    try:
        # Split on commas, strip spaces, and convert to float
        values = [float(x.strip()) for x in text.split(",")]

        if len(values) == 0:
            raise ValueError("You must enter at least one score.")

        return values

    except ValueError:
        # Generic error if conversion to float fails
        raise ValueError(
            "Scores must be numbers separated by commas. "
            "Example: 10, 12.5, 9"
        )


def create_dataframe(subject1_name, subject2_name, scores1, scores2):
    """
    Create a pandas DataFrame from the two subject score lists.

    The DataFrame will look something like this:

                    Math  Science
        Student 1   90.0    85.0
        Student 2   78.0    88.0
        ...

    We also validate that the number of scores is the same for both subjects.
    """
    if len(scores1) != len(scores2):
        raise ValueError(
            f"Both subjects must have the SAME number of scores.\n"
            f"{subject1_name} has {len(scores1)} scores but "
            f"{subject2_name} has {len(scores2)} scores."
        )

    num_students = len(scores1)

    # Create index labels: "Student 1", "Student 2", ...
    student_labels = [f"Student {i + 1}" for i in range(num_students)]

    # Build a DataFrame: columns are subject names, index is student labels
    df = pd.DataFrame(
        {
            subject1_name: scores1,
            subject2_name: scores2
        },
        index=student_labels
    )

    return df


def plot_grouped_bar(df, plot_frame):
    """
    Create a grouped bar chart from the pandas DataFrame and display it
    inside the given Tkinter frame (plot_frame).

    The DataFrame is expected to have:
        - rows: students
        - columns: two subjects (e.g., Math, Science)
    """
    # Clear any existing plot in the frame by destroying all children
    for child in plot_frame.winfo_children():
        child.destroy()

    # Subject names are the DataFrame's columns
    subject_names = list(df.columns)
    subject1_name = subject_names[0]
    subject2_name = subject_names[1]

    # Number of students / data points
    n = len(df)

    # X positions for each student
    x = np.arange(n)

    # Bar width
    bar_width = 0.35

    # Create a new matplotlib Figure and Axes
    fig, ax = plt.subplots(figsize=(8, 5))

    # Bars for subject 1 (shifted left)
    ax.bar(
        x - bar_width / 2,
        df[subject1_name],
        width=bar_width,
        label=subject1_name
    )

    # Bars for subject 2 (shifted right)
    ax.bar(
        x + bar_width / 2,
        df[subject2_name],
        width=bar_width,
        label=subject2_name
    )

    # Set labels and title
    ax.set_xlabel("Students")
    ax.set_ylabel("Scores")
    ax.set_title("Grouped Bar Chart: Subject Score Comparison")

    # Use the DataFrame index ("Student 1", "Student 2", ...) for x-axis labels
    ax.set_xticks(x)
    ax.set_xticklabels(df.index, rotation=45)

    # Add gridlines on y-axis to help reading the graph
    ax.grid(axis="y", linestyle="--", alpha=0.6)

    # Show legend to identify the two subjects
    ax.legend()

    # Adjust layout so labels don’t get cut off
    fig.tight_layout()

    # Embed the figure into the Tkinter frame using FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()

    # Get the Tkinter widget from the canvas and pack it
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)


# ---------- MAIN APPLICATION LOGIC (GUI SETUP) ----------

def on_plot_button_click():
    """
    This function runs when the "Create Graph" button is clicked.

    It:
        1. Reads the input from the GUI
        2. Parses the scores
        3. Builds a pandas DataFrame
        4. Calls the plotting function

    Any errors are shown in a pop-up message box.
    """
    # Get text from the input fields
    subject1_name = entry_subject1.get().strip()
    subject2_name = entry_subject2.get().strip()
    scores1_text = entry_scores1.get().strip()
    scores2_text = entry_scores2.get().strip()

    # Basic validation of subject names
    if not subject1_name:
        messagebox.showerror("Input Error", "Please enter a name for Subject 1.")
        return

    if not subject2_name:
        messagebox.showerror("Input Error", "Please enter a name for Subject 2.")
        return

    try:
        # Convert the score strings into lists of floats
        scores1 = parse_scores(scores1_text)
        scores2 = parse_scores(scores2_text)

        # Create a pandas DataFrame with validation
        df = create_dataframe(subject1_name, subject2_name, scores1, scores2)

        # Plot the grouped bar chart in the plot frame
        plot_grouped_bar(df, frame_plot)

    except ValueError as ve:
        # Show any validation or parsing errors to the user
        messagebox.showerror("Input Error", str(ve))

    except Exception as e:
        # Catch any unexpected errors (good practice in student code)
        messagebox.showerror("Unexpected Error", f"Something went wrong:\n{e}")


# ---------- BUILDING THE TKINTER WINDOW ----------

# Create the main window
root = tk.Tk()
root.title("Grouped Bar Graph with pandas and Tkinter")

# Optional: set a minimum size for the window
root.minsize(700, 500)

# Main container frame
frame_main = tk.Frame(root, padx=10, pady=10)
frame_main.pack(fill=tk.BOTH, expand=True)

# ------- Top instructions label -------
label_instructions = tk.Label(
    frame_main,
    text=(
        "Enter two subject names and their scores (comma-separated).\n"
        "Example scores: 90, 85, 78, 92"
    ),
    justify=tk.LEFT
)
label_instructions.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

# ------- Subject 1 input -------
label_subject1 = tk.Label(frame_main, text="Subject 1 name:")
label_subject1.grid(row=1, column=0, sticky="e", padx=(0, 5), pady=2)

entry_subject1 = tk.Entry(frame_main, width=30)
entry_subject1.grid(row=1, column=1, sticky="w", pady=2)

label_scores1 = tk.Label(frame_main, text="Subject 1 scores:")
label_scores1.grid(row=2, column=0, sticky="e", padx=(0, 5), pady=2)

entry_scores1 = tk.Entry(frame_main, width=50)
entry_scores1.grid(row=2, column=1, sticky="w", pady=2)

# ------- Subject 2 input -------
label_subject2 = tk.Label(frame_main, text="Subject 2 name:")
label_subject2.grid(row=3, column=0, sticky="e", padx=(0, 5), pady=2)

entry_subject2 = tk.Entry(frame_main, width=30)
entry_subject2.grid(row=3, column=1, sticky="w", pady=2)

label_scores2 = tk.Label(frame_main, text="Subject 2 scores:")
label_scores2.grid(row=4, column=0, sticky="e", padx=(0, 5), pady=2)

entry_scores2 = tk.Entry(frame_main, width=50)
entry_scores2.grid(row=4, column=1, sticky="w", pady=2)

# ------- Plot button -------
button_plot = tk.Button(
    frame_main,
    text="Create Graph",
    command=on_plot_button_click
)
button_plot.grid(row=5, column=0, columnspan=2, pady=10)

# ------- Frame to hold the plot -------
frame_plot = tk.Frame(frame_main, borderwidth=2, relief=tk.GROOVE)
frame_plot.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=(10, 0))

# Make the plot frame expandable when the window is resized
frame_main.rowconfigure(6, weight=1)
frame_main.columnconfigure(1, weight=1)

# Start the Tkinter event loop (this keeps the window open)
root.mainloop()
