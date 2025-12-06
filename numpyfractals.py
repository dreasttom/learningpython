"""
fractal_numpy_demo.py

Educational fractal generator using NumPy.

This script is designed for STUDENTS:
    - It uses NumPy arrays and vectorization instead of slow Python loops.
    - It creates two classic fractals:
        1) Mandelbrot set
        2) Julia set (for a chosen complex parameter c)
    - It includes a simple text-based menu.
    - It is heavily commented to explain the math AND the NumPy usage.

REQUIREMENTS:
    - numpy
    - matplotlib

    Install with:
        pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt


# ================================================================
# HELPER: INPUT WITH DEFAULT (FOR SIMPLE “MENU” INTERACTION)
# ================================================================

def input_with_default(prompt, default, cast_type=float):
    """
    Ask the user for a value, but allow them to just press ENTER
    to keep a default.

    Parameters
    ----------
    prompt : str
        Text shown to the user.
    default : any
        Default value used if the user presses ENTER.
    cast_type : callable
        Function used to convert the input string (e.g. float, int, str).

    Returns
    -------
    value : same type as 'default'
    """
    full_prompt = f"{prompt} [default = {default}]: "
    s = input(full_prompt)

    # If user presses ENTER with no text, return the default
    if s.strip() == "":
        return default

    try:
        return cast_type(s)
    except ValueError:
        print("Invalid input. Using default value.")
        return default


# ================================================================
# MANDELBROT SET GENERATION
# ================================================================

def compute_mandelbrot(width, height,
                       x_min=-2.5, x_max=1.0,
                       y_min=-1.5, y_max=1.5,
                       max_iter=100):
    """
    Compute a Mandelbrot set image using NumPy.

    The Mandelbrot set is defined in the complex plane.

    For each point c = x + i y:
        We iterate:
            z_{n+1} = z_n^2 + c
        starting at z_0 = 0.

        If the magnitude |z_n| stays bounded (doesn't escape to infinity)
        after many iterations, we say that c belongs to the Mandelbrot set.

        In practice, we:
            - Run up to max_iter iterations.
            - If |z| exceeds 2, we consider it "escaped".
            - The iteration count where it escapes is used for coloring.

    This function returns an array 'escape_counts' of shape (height, width),
    where each entry is the iteration at which that point escaped, or
    max_iter if it never escaped.

    IMPORTANT: We use NumPy to do this for *all points at once* (vectorization),
    instead of looping over pixels in Python. This is much faster and more
    "NumPy-ish".
    """
    # 1. Create a grid of (x, y) values spanning the rectangular region
    #    in the complex plane.
    #
    #    np.linspace(start, stop, num) creates 'num' evenly spaced values
    #    between start and stop (inclusive).
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    # 2. Turn the 1D arrays x and y into 2D coordinate grids X and Y.
    #
    #    X will have shape (height, width), with each row being a copy of x.
    #    Y will have shape (height, width), with each column being a copy of y.
    X, Y = np.meshgrid(x, y)

    # 3. Combine X and Y into a complex array C = X + iY.
    #
    #    In NumPy, the imaginary unit is represented by 1j.
    C = X + 1j * Y

    # 4. Initialize Z to zero (same shape as C). This represents z_0 = 0
    #    for every point in the grid.
    Z = np.zeros_like(C, dtype=np.complex128)

    # 5. Initialize an array to store the "escape iteration" for each point.
    #
    #    Start with all zeros. We'll fill this with the iteration number
    #    on which each point escaped.
    escape_counts = np.zeros(C.shape, dtype=int)

    # 6. This mask tells us which points are still being iterated (i.e.
    #    which points haven't escaped yet).
    #
    #    Start with all True, then as points escape we set them to False.
    mask = np.ones(C.shape, dtype=bool)

    # 7. Iterate the Mandelbrot formula up to max_iter times.
    for iter_num in range(1, max_iter + 1):
        # Only update points that are still "alive" (mask == True).
        # This avoids unnecessary computation for points that already escaped.
        Z[mask] = Z[mask] ** 2 + C[mask]

        # Check which of those points now have |Z| > 2 (i.e., have escaped).
        escaped_now = np.abs(Z) > 2

        # For points that just escaped (mask was True, but abs(Z)>2 now),
        # record the iteration number.
        #
        # We only want to record the first time each point escapes, so
        # we only update where mask is True.
        newly_escaped = escaped_now & mask
        escape_counts[newly_escaped] = iter_num

        # Update mask: points that escaped are no longer iterated.
        mask[newly_escaped] = False

        # Optional: if no points are left, we can break early.
        if not mask.any():
            break

    # Points that never escaped have escape_counts = 0.
    # For visual purposes we can set those to max_iter.
    escape_counts[escape_counts == 0] = max_iter

    return escape_counts


def plot_mandelbrot(escape_counts,
                    x_min=-2.5, x_max=1.0,
                    y_min=-1.5, y_max=1.5,
                    title="Mandelbrot Set"):
    """
    Plot the Mandelbrot escape counts using matplotlib.

    We use imshow to display a 2D array as an image.

    Parameters
    ----------
    escape_counts : 2D array
        Iteration counts returned by compute_mandelbrot().
    x_min, x_max, y_min, y_max : float
        Region of the complex plane (for axis labels).
    title : str
        Title of the plot.
    """
    plt.figure(figsize=(8, 6))

    # imshow expects (rows, cols) → (y, x).
    # extent defines the coordinate system of the image.
    plt.imshow(escape_counts,
               extent=[x_min, x_max, y_min, y_max],
               origin="lower",
               cmap="magma")  # 'magma' is a pretty colormap

    plt.colorbar(label="Escape iteration")
    plt.xlabel("Real axis")
    plt.ylabel("Imaginary axis")
    plt.title(title)
    plt.tight_layout()
    plt.show()


# ================================================================
# JULIA SET GENERATION
# ================================================================

def compute_julia(width, height,
                  x_min=-1.5, x_max=1.5,
                  y_min=-1.5, y_max=1.5,
                  c_real=-0.7, c_imag=0.27015,
                  max_iter=100):
    """
    Compute a Julia set image using NumPy.

    A Julia set is similar to the Mandelbrot set, but with a twist.

    For each point z_0 = x + i y (in the complex plane), we iterate:
        z_{n+1} = z_n^2 + c

    where 'c' is a fixed complex number (chosen by us).

    Depending on the value of c, we get different beautiful shapes.

    Just like the Mandelbrot computation:
        - If |z| stays bounded, the point is in the Julia set.
        - We track the iteration at which |z| first exceeds 2.

    Parameters
    ----------
    width, height : int
        Size of the image in pixels.
    x_min, x_max, y_min, y_max : float
        Region of the complex plane.
    c_real, c_imag : float
        Real and imaginary parts of the constant c.
    max_iter : int
        Maximum number of iterations.

    Returns
    -------
    escape_counts : 2D array of ints
        Iteration at which each point escaped.
    """
    # Create grid in the complex plane, as before.
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Constant complex number c
    c = complex(c_real, c_imag)

    escape_counts = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)

    for iter_num in range(1, max_iter + 1):
        # Apply z_{n+1} = z_n^2 + c only where mask is True
        Z[mask] = Z[mask] ** 2 + c

        # Check for escape
        escaped_now = np.abs(Z) > 2
        newly_escaped = escaped_now & mask
        escape_counts[newly_escaped] = iter_num
        mask[newly_escaped] = False

        if not mask.any():
            break

    escape_counts[escape_counts == 0] = max_iter
    return escape_counts


def plot_julia(escape_counts,
               x_min=-1.5, x_max=1.5,
               y_min=-1.5, y_max=1.5,
               title="Julia Set"):
    """
    Plot a Julia set image from 'escape_counts'.

    Parameters
    ----------
    escape_counts : 2D array
        Iteration counts from compute_julia().
    x_min, x_max, y_min, y_max : float
        Region of the complex plane (for axes).
    title : str
        Plot title.
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(escape_counts,
               extent=[x_min, x_max, y_min, y_max],
               origin="lower",
               cmap="plasma")
    plt.colorbar(label="Escape iteration")
    plt.xlabel("Real axis")
    plt.ylabel("Imaginary axis")
    plt.title(title)
    plt.tight_layout()
    plt.show()


# ================================================================
# SIMPLE TEXT-BASED MENU (FOR STUDENT INTERACTION)
# ================================================================

def run_mandelbrot_menu():
    """
    Ask the user for Mandelbrot parameters and plot the fractal.
    """
    print("\n=== Mandelbrot Set ===\n")
    width = input_with_default("Image width (pixels)", 800, int)
    height = input_with_default("Image height (pixels)", 600, int)
    max_iter = input_with_default("Max iterations", 100, int)

    print("\nRegion of complex plane to display:")
    x_min = input_with_default("x_min", -2.5, float)
    x_max = input_with_default("x_max", 1.0, float)
    y_min = input_with_default("y_min", -1.5, float)
    y_max = input_with_default("y_max", 1.5, float)

    print("\nComputing Mandelbrot set (this might take a few seconds)...")
    escape_counts = compute_mandelbrot(width, height,
                                       x_min=x_min, x_max=x_max,
                                       y_min=y_min, y_max=y_max,
                                       max_iter=max_iter)

    plot_mandelbrot(escape_counts,
                    x_min=x_min, x_max=x_max,
                    y_min=y_min, y_max=y_max,
                    title=f"Mandelbrot Set (max_iter={max_iter})")


def run_julia_menu():
    """
    Ask the user for Julia set parameters and plot the fractal.
    """
    print("\n=== Julia Set ===\n")
    width = input_with_default("Image width (pixels)", 800, int)
    height = input_with_default("Image height (pixels)", 600, int)
    max_iter = input_with_default("Max iterations", 100, int)

    print("\nRegion of complex plane to display:")
    x_min = input_with_default("x_min", -1.5, float)
    x_max = input_with_default("x_max", 1.5, float)
    y_min = input_with_default("y_min", -1.5, float)
    y_max = input_with_default("y_max", 1.5, float)

    print("\nComplex constant c = c_real + i*c_imag:")
    c_real = input_with_default("c_real", -0.7, float)
    c_imag = input_with_default("c_imag", 0.27015, float)

    print("\nComputing Julia set (this might take a few seconds)...")
    escape_counts = compute_julia(width, height,
                                  x_min=x_min, x_max=x_max,
                                  y_min=y_min, y_max=y_max,
                                  c_real=c_real, c_imag=c_imag,
                                  max_iter=max_iter)

    plot_julia(escape_counts,
               x_min=x_min, x_max=x_max,
               y_min=y_min, y_max=y_max,
               title=f"Julia Set (c={c_real}+{c_imag}i, max_iter={max_iter})")


def main_menu():
    """
    Simple text-based menu for choosing which fractal to generate.

    This function loops until the user chooses to quit.
    """
    while True:
        print("\n====================================")
        print("      NumPy Fractal Generator       ")
        print("====================================")
        print("1) Mandelbrot set")
        print("2) Julia set")
        print("3) Quit")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == "1":
            run_mandelbrot_menu()
        elif choice == "2":
            run_julia_menu()
        elif choice == "3":
            print("\nExiting fractal generator. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")


# ================================================================
# ENTRY POINT
# ================================================================

if __name__ == "__main__":
    main_menu()
