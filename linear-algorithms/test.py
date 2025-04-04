from gauss_elimination_method import GaussEliminationMethod
from gauss_jordan_method import GaussJordanMethod
from gauss_seidel_iterative_method import GaussSeidelIterativeMethod
from jacobi_iterative_method import JacobiIterativeMethod
from lu_decomposition_method import LUDecomposition

coefficient_matrix = [
    [13, 17, 18, 14, 15],
    [14, 12, 10, 9, 11],
    [1, 2, 26, 30, 31],
    [9, 19, 21, 22, 24],
    [30, 20, 51, 4, 3]
]
constant_matrix = [[1], [1], [1], [1], [1]]

print(f"Gauss Elimination Method:\n")
gauss_elimination_roots = GaussEliminationMethod().solve(coefficient_matrix, constant_matrix)

print(f"Gauss Jordan Method:\n")
gauss_jordan_roots = GaussJordanMethod().solve(coefficient_matrix, constant_matrix)

print(f"LU Decomposition Method:\n")
L, U, Y, X = LUDecomposition().solve(coefficient_matrix, constant_matrix)

"""
For Jacobi's iterative method and Gauss Siedel iterative method, the coefficient matrix needs to be diagonally
dominant.
"""

diagonally_dominant_coefficient_matrix = [
    [6, 2, -1],
    [1, 5, 1],
    [2, 1, 4]
]
constant_matrix = [[4], [3], [27]]

print(f"Jacobi's Iterative Method:\n")
jacobi_iterative_method_roots = JacobiIterativeMethod().solve(8,
                                                              diagonally_dominant_coefficient_matrix.copy(),
                                                              constant_matrix.copy())

print(f"Gauss Seidel Iterative Method:\n")
gauss_seidel_iterative_method_roots = GaussSeidelIterativeMethod().solve(4,
                                                                         diagonally_dominant_coefficient_matrix.copy(),
                                                                         constant_matrix.copy())