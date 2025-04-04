# Python Numerical Computing Utils

This repository houses various mathematical algorithms for computing the roots of matrices and non-linear equations, coded in Python using standard libraries.

## Table of Contents

- [Description](#description)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

This repository contains Python implementations of several numerical algorithms for solving mathematical problems such as computing the roots of matrices and solving non-linear equations. The primary goal is to provide efficient and easy-to-use solutions using standard Python libraries.

## Repository Structure

The repository is organized as follows:

```
python-numerical-computing-utils/
│
├── linear-algorithms/
│   ├── gauss_elimination_method.py
│   ├── gauss_jordan_method.py
│   ├── gauss_seidel_iterative_method.py
│   ├── jacobi_iterative_method.py
│   ├── lu_decomposition_method.py
│   └── test.py 
│
├── non-linear-algorithms/
│   ├── bisection_method.py
│   ├── fixed_point_iteration_method.py
│   ├── newton_raphson_method.py
│   ├── regula_falsi_method.py
│   ├── regula_secant_method.py
│   └── test.py
│
└── README.md
```

- **linear-algorithms/**: Contains the implementation of various numerical algorithms for solving matrices.
  - `gauss_elimination_method.py`: Class for computing the roots of matrices using the Gauss Elimination method.
  - `gauss_jordan_method.py`: Class for computing the roots of matrices using the Gauss-Jordan method.
  - `gauss_seidel_iterative_method.py`: Class for computing the roots of matrices using the Gauss-Seidel Iterative method.
  - `jacobi_iterative_method.py`: Class for computing the roots of matrices using the Jacobi Iterative method.
  - `lu_decomposition_method.py`: Class for computing the roots of matrices using the LU Decomposition method.
- **non-linear-algorithms/**: Contains the implementation of various numerical algorithms for computing the roots of non-linear equations.
  - `bisection_method.py`: Class for computing the roots of non-linear equations using the Bisection method.
  - `fixed_point_iteration_method.py`: Class for computing the roots of non-linear equations using the Fixed Point Iteration method.
  - `newton_raphson_method.py`: Class for computing the roots of non-linear equations using the Newton-Raphson method.
  - `regula_falsi_method.py`: Class for computing the roots of non-linear equations using the Gauss Regula-Falsi method.
  - `regula_secant_method.py`: Class for computing the roots of non-linear equations using the Gauss Regula-Secant method.

## Installation

Not publishing this repository as a package yet. Just download the scripts and use them. If this repository proves beneficial to a decent amount of people, then I'll 
publish it as a package.

## Usage

View the test.py files in both sub-folders for usage examples.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes. Would also appreciate it if you guys could
populate this repository with more algorithms.

## License

No license. Would appreciate attribution though.
