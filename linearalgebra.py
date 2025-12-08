"""
SciPy Linear Algebra Demo for Students

This script demonstrates several core linear algebra operations using SciPy:

- Creating matrices and vectors with NumPy
- Matrix properties: shape, rank, determinant
- Solving linear systems Ax = b
- Computing eigenvalues and eigenvectors
- Computing matrix inverses and pseudoinverses
- Performing Singular Value Decomposition (SVD)

It is designed as a TEACHING AID:
- Extensive comments explain what each part does.
- Basic error handling is included to show good practice.

REQUIREMENTS (install via pip if needed):
    pip install numpy scipy

RUN:
    python scipy_linear_algebra_demo.py
    # or with a custom matrix size:
    python scipy_linear_algebra_demo.py --size 3
"""

import sys
import argparse

# --- Handle imports safely with error messages -------------------------------
try:
    import numpy as np
except ImportError:
    print("ERROR: NumPy is not installed. Install it with 'pip install numpy'.")
    sys.exit(1)

try:
    from scipy import linalg
except ImportError:
    print("ERROR: SciPy is not installed. Install it with 'pip install scipy'.")
    sys.exit(1)


# --------------------------------------------------------------------------- #
# Helper Functions
# --------------------------------------------------------------------------- #

def create_example_system(n: int = 3):
    """
    Create an example linear system Ax = b.

    Parameters
    ----------
    n : int
        Size of the square matrix A (n x n). Default is 3.

    Returns
    -------
    A : np.ndarray
        An n x n matrix.
    b : np.ndarray
        An n-dimensional vector.
    """
    # For teaching, we use a fixed random seed so results are reproducible.
    np.random.seed(42)

    # Create a random n x n matrix
    A = np.random.randint(low=1, high=10, size=(n, n)).astype(float)

    # Create a random n-dimensional vector
    b = np.random.randint(low=1, high=10, size=(n,)).astype(float)

    return A, b


def print_matrix_info(A: np.ndarray, name: str = "A"):
    """
    Print basic information about a matrix: shape, rank, determinant (if square).

    Parameters
    ----------
    A : np.ndarray
        The matrix to inspect.
    name : str
        A label for the matrix (for printing).
    """
    print(f"\n--- Basic info for matrix {name} ---")
    print(f"{name} =\n{A}")
    print(f"Shape of {name}: {A.shape}")

    # Compute the rank using SciPy's linear algebra module.
    try:
        rank = linalg.matrix_rank(A)
        print(f"Rank of {name}: {rank}")
    except Exception as e:
        print(f"Could not compute rank of {name}: {e}")

    # If A is square, compute the determinant.
    if A.shape[0] == A.shape[1]:
        try:
            det = linalg.det(A)
            print(f"Determinant of {name}: {det:.4f}")
        except Exception as e:
            print(f"Could not compute determinant of {name}: {e}")
    else:
        print(f"{name} is not a square matrix, so determinant is not defined.")


def solve_linear_system(A: np.ndarray, b: np.ndarray):
    """
    Solve the linear system Ax = b using SciPy.

    Parameters
    ----------
    A : np.ndarray
        Coefficient matrix.
    b : np.ndarray
        Right-hand side vector.

    Returns
    -------
    x : np.ndarray or None
        The solution vector, or None if the system could not be solved.
    """
    print("\n--- Solving the linear system A x = b ---")
    print("A =\n", A)
    print("b =\n", b)

    # Make sure dimensions are compatible for Ax = b.
    if A.shape[0] != A.shape[1]:
        print("ERROR: A must be square to use 'linalg.solve'.")
        return None
    if A.shape[0] != b.shape[0]:
        print("ERROR: Dimensions of A and b do not match.")
        return None

    try:
        # Solve Ax = b
        x = linalg.solve(A, b)
    except linalg.LinAlgError as e:
        # This may happen if A is singular (determinant=0)
        print(f"ERROR: Could not solve Ax = b: {e}")
        print("Hint: The matrix might be singular (non-invertible).")
        return None

    print("\nSolution x to A x = b is:\n", x)

    # Check the solution by computing Ax and comparing with b.
    b_hat = A @ x  # matrix-vector multiplication
    residual = b_hat - b
    residual_norm = np.linalg.norm(residual)

    print("\nCheck: A x =\n", b_hat)
    print("Original b =\n", b)
    print(f"Residual (A x - b) =\n{residual}")
    print(f"Norm of residual: {residual_norm:.4e}")

    return x


def compute_eigen(A: np.ndarray):
    """
    Compute eigenvalues and eigenvectors of a square matrix A.

    Parameters
    ----------
    A : np.ndarray
        Square matrix.

    Returns
    -------
    w : np.ndarray
        Eigenvalues.
    v : np.ndarray
        Eigenvectors (columns of v are the eigenvectors).
    """
    print("\n--- Eigenvalues and Eigenvectors ---")

    # Eigenvalues are only defined for square matrices.
    if A.shape[0] != A.shape[1]:
        print("ERROR: A must be square to compute eigenvalues.")
        return None, None

    try:
        # linalg.eig returns (eigenvalues, eigenvectors)
        w, v = linalg.eig(A)
    except linalg.LinAlgError as e:
        print(f"ERROR: Could not compute eigenvalues/eigenvectors: {e}")
        return None, None

    print("Matrix A =\n", A)
    print("\nEigenvalues of A:\n", w)
    print("\nEigenvectors of A (each column is an eigenvector):\n", v)

    # Demonstrate the eigenvalue equation A v = λ v for the first eigenpair
    if w is not None and len(w) > 0:
        lam = w[0]
        vec = v[:, 0]
        left = A @ vec
        right = lam * vec

        print("\nCheck eigenvalue/eigenvector for the first eigenpair:")
        print("A @ v_0 =\n", left)
        print("λ_0 * v_0 =\n", right)
        print("Difference:\n", left - right)

    return w, v


def compute_inverse_and_pinv(A: np.ndarray):
    """
    Compute the inverse and pseudoinverse of a matrix.

    Parameters
    ----------
    A : np.ndarray
        The matrix to invert (if possible).
    """
    print("\n--- Matrix inverse and pseudoinverse ---")
    print("A =\n", A)

    # Compute inverse (only for square, non-singular matrices)
    if A.shape[0] == A.shape[1]:
        try:
            A_inv = linalg.inv(A)
            print("\nInverse of A (A^{-1}) =\n", A_inv)

            # Check that A * A^{-1} ≈ I
            I_approx = A @ A_inv
            print("\nA @ A^{-1} ≈ I:\n", I_approx)
        except linalg.LinAlgError as e:
            print(f"ERROR: Could not compute inverse of A: {e}")
            print("Hint: A might be singular (determinant is zero).")
    else:
        print("A is not square; a standard inverse does not exist.")

    # Compute Moore-Penrose pseudoinverse (always defined)
    try:
        A_pinv = linalg.pinv(A)
        print("\nMoore-Penrose pseudoinverse of A (A^+) =\n", A_pinv)
    except Exception as e:
        print(f"ERROR: Could not compute pseudoinverse of A: {e}")


def demonstrate_svd(A: np.ndarray):
    """
    Demonstrate Singular Value Decomposition (SVD).

    SVD factors A into U, s, Vh such that:
        A = U @ np.diag(s) @ Vh

    Parameters
    ----------
    A : np.ndarray
        Matrix to decompose (can be rectangular).
    """
    print("\n--- Singular Value Decomposition (SVD) ---")
    print("A =\n", A)

    try:
        # full_matrices=False gives the "economy" SVD, which is often easier to interpret
        U, s, Vh = linalg.svd(A, full_matrices=False)
    except linalg.LinAlgError as e:
        print(f"ERROR: Could not compute SVD of A: {e}")
        return

    print("\nMatrix U (left singular vectors) =\n", U)
    print("\nSingular values s =\n", s)
    print("\nMatrix Vh (right singular vectors, transposed) =\n", Vh)

    # Reconstruct A from U, s, Vh to show that SVD works.
    Sigma = np.diag(s)  # convert singular values into a diagonal matrix
    A_reconstructed = U @ Sigma @ Vh
    print("\nReconstructed A from SVD (U @ Σ @ Vh) =\n", A_reconstructed)

    # Show reconstruction error (should be very small)
    reconstruction_error = np.linalg.norm(A - A_reconstructed)
    print(f"\nReconstruction error ||A - U Σ Vh|| = {reconstruction_error:.4e}")


# --------------------------------------------------------------------------- #
# Main function: ties everything together
# --------------------------------------------------------------------------- #

def main():
    # Use argparse to allow the user to specify matrix size from the command line.
    parser = argparse.ArgumentParser(
        description="Demonstrate linear algebra operations using SciPy."
    )
    parser.add_argument(
        "--size",
        type=int,
        default=3,
        help="Size of the square matrix A (default: 3). Should be between 2 and 8.",
    )
    args = parser.parse_args()

    n = args.size

    # Basic validation of the size parameter.
    if n < 2 or n > 8:
        print("ERROR: Matrix size '--size' should be between 2 and 8.")
        sys.exit(1)

    print("=========================================")
    print(" SciPy Linear Algebra Demo for Students")
    print("=========================================")
    print(f"Using matrix size n = {n}")

    # Create example system
    A, b = create_example_system(n)

    # Show matrix and basic properties
    print_matrix_info(A, name="A")

    # Solve A x = b
    x = solve_linear_system(A, b)

    # Compute eigenvalues and eigenvectors
    compute_eigen(A)

    # Show inverse and pseudoinverse
    compute_inverse_and_pinv(A)

    # Demonstrate SVD (works for square or rectangular matrices)
    demonstrate_svd(A)

    print("\n=== Demo complete. ===")


if __name__ == "__main__":
    main()
