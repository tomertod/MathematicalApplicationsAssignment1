# Mathematical Applications - Assignment 1
## Numerical Methods: Secant Method & Gaussian Elimination

### Submitting Students:
* Tomer Todria - 318784709
* Asaf Katz - 323841338

---

### Project Description
This project implements two fundamental numerical algorithms in Python, focusing on root-finding and linear algebra operations without the use of external libraries like NumPy.

---

### Implementation Details

#### Part 1: Secant Method
The `Secant_method` function implements an iterative numerical technique used to find the root (zero) of a continuous function $f(x)$. 
* **Input:** A mathematical function (string), and two initial guesses ($x_0, x_1$) that are close to the expected root.
* **Logic:** The function calculates the next approximation by finding the intersection of the secant line passing through $(x_{n-1}, f(x_{n-1}))$ and $(x_n, f(x_n))$ with the x-axis.
* **Termination:** The process continues until the difference between iterations is smaller than epsilon ($0.001$) or until a maximum of $30$ iterations is reached.

#### Part 2: Gaussian Elimination (Matrix Reduction)
The `ge` function reduces a given matrix to its Upper Triangular Form (Row Echelon Form) using the Gaussian Elimination algorithm.
* **Input:** A matrix represented as a list of lists of floats (dimension $m \times n$).
* **Logic:** 1. **Pivoting:** If the diagonal element $(i, i)$ is zero, the function swaps the current row with a lower row that has a non-zero element in the same column.
    2. **Normalization:** Divides the current row by the pivot element to set the diagonal to $1$.
    3. **Elimination:** Subtracts the normalized row from all lower rows to create zeros below the diagonal.
* **Constraints:** Implemented using only built-in Python functions, strictly avoiding external matrix libraries as per the assignment requirements.

---

### How to Run
1. Ensure you have Python 3.x installed.
2. Place the script and any required input files in the same directory.
3. Run the script using:
   ```
   python assignment1.py
   ```
