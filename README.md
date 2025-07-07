# Python Numerical Computing Utils

A comprehensive collection of Python implementations for fundamental numerical methods used in scientific computing, engineering, and applied mathematics. This repository serves as a learning resource and practical toolbox for solving problems involving linear systems, nonlinear equations, numerical differentiation, integration, and interpolation.

---

## Features

- **Linear Algorithms**: Methods for solving linear systems, including direct and iterative techniques.
- **Non-Linear Algorithms**: Root-finding methods for nonlinear equations.
- **Numerical Differentiation**: Techniques for approximating derivatives.
- **Numerical Integration**: Methods for evaluating definite integrals numerically.
- **Numerical Interpolation**: Algorithms for constructing new data points within the range of a discrete set.

---

## Directory Structure

```
python-numerical-computing-utils/
│
├── linear-algorithms/
│   ├── gauss_elimination_method.py         # Classical Gauss Elimination for linear systems
│   ├── gauss_jordan_method.py              # Gauss-Jordan elimination (row reduction)
│   ├── gauss_seidel_iterative_method.py    # Gauss-Seidel iterative solver
│   ├── jacobi_iterative_method.py          # Jacobi iterative solver
│   ├── lu_decomposition_method.py          # LU decomposition for matrix factorization
│   ├── test.py                            # Tests for linear algorithms
│   └── .gitignore
│
├── non-linear-algorithms/
│   ├── bisection_method.py                 # Bisection root-finding method
│   ├── fixed_point_iteration_method.py     # Fixed-point iteration for roots
│   ├── newton_raphson_method.py            # Newton-Raphson method for nonlinear equations
│   ├── regula_falsi_method.py              # Regula Falsi (False Position) method
│   ├── regula_secant_method.py             # Secant method for root finding
│   ├── test.py                            # Tests for non-linear algorithms
│   └── .gitignore
│
├── numerical-differentiation/
│   ├── backward_differentiation.py         # Backward finite difference for derivatives
│   ├── forward_differentiation.py          # Forward finite difference for derivatives
│   ├── test.py                            # Tests for numerical differentiation
│   └── .gitignore
│
├── numerical-integration/
│   ├── simpsons_one_by_three_rule.py       # Simpson's 1/3 rule for integration
│   ├── simpsons_three_by_eight_rule.py     # Simpson's 3/8 rule for integration
│   ├── trapzoidals_rule.py                 # Trapezoidal rule for integration
│   ├── test.py                            # Tests for numerical integration
│   └── .gitignore
│
├── numerical-interpolation/
│   ├── gauss_forward_central_difference.py # Gauss forward central difference interpolation
│   ├── lagrange_interpolation.py           # Lagrange polynomial interpolation
│   ├── newtons_backward_difference.py      # Newton's backward difference interpolation
│   ├── newtons_divided_difference.py       # Newton's divided difference interpolation
│   ├── newtons_forward_difference.py       # Newton's forward difference interpolation
│   ├── test.py                            # Tests for numerical interpolation
│   └── .gitignore
│
└── README.md                               # Project documentation (this file)
```

---

## Module Overview

### Linear Algorithms
- **Direct Methods**: `gauss_elimination_method.py`, `gauss_jordan_method.py`, `lu_decomposition_method.py`
- **Iterative Methods**: `jacobi_iterative_method.py`, `gauss_seidel_iterative_method.py`
- **Testing**: `test.py` for unit tests and usage examples

### Non-Linear Algorithms
- Root-finding: Bisection, Fixed-point, Newton-Raphson, Regula Falsi, Secant methods
- All implementations include test scripts for validation

### Numerical Differentiation
- Forward and backward finite difference methods for approximating derivatives of functions
- Accompanied by test scripts

### Numerical Integration
- Trapezoidal rule, Simpson’s 1/3 and 3/8 rules for numerical integration of functions
- Includes tests for demonstration

### Numerical Interpolation
- Lagrange and Newton methods for interpolation of discrete data
- Gauss forward central difference for interpolation
- Example and test scripts included

---

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/PythoneerSamurai/python-numerical-computing-utils.git
   cd python-numerical-computing-utils
   ```

2. **Run Tests or Examples**
   - Each submodule contains a `test.py` file to demonstrate usage.

3. **Dependencies**
   - Only standard Python libraries used (unless noted in the script headers).

---

## Contribution

Issues, improvements, and new numerical algorithms are welcome! Please open an issue or submit a pull request.

---

## License

[CC BY License](https://creativecommons.org/licenses/by/4.0/).

---

## Author

[PythoneerSamurai](https://github.com/PythoneerSamurai)
