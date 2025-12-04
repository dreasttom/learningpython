import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# The purpose of this code  is just to introduce you to the tkinter library


def greeting():
    try:
        name = name_entry.get()
        if name:
            messagebox.showinfo("greetinging", f"Hello, {name}!")
        else:
            messagebox.showwarning("Warning", "Please enter your name.")
    except:
        print("There was an error in the greetinging function")
# Create the main window
window = tk.Tk()
window.title("Tkinter Example")

# Create a label
label = ttk.Label(window, text="What is your name?")
label.pack(pady=10)

# Create an entry widget
name_entry = ttk.Entry(window)
name_entry.pack(pady=5)

# Create a button
greeting_button = ttk.Button(window, text="Greeting", command=greeting)
greeting_button.pack(pady=10)

# Create a combobox
options = ["Option 1", "Option 2", "Option 3"]
combo = ttk.Combobox(window, values=options)
combo.pack(pady=5)

# Create a progressbar
progress_bar = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=10)

# Function to simulate progress
def simulate_progress():
    for i in range(101):
        progress_bar["value"] = i
        window.update_idletasks()  # Update the GUI
        window.after(50)  # Simulate progress on the progress bar

# Create a button to start the progress
start_button = ttk.Button(window, text="Start Progress", command=simulate_progress)
start_button.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()
