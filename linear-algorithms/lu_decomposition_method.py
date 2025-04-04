
class LUDecomposition:
    def __init__(self):
        # Empty Constructor function, nothing to initialize.
        pass

    def lower_eliminator(
            self,
            row: int,
            column: int,
            pivot_element: int or float,
            lower: int or float,
            lowers: int,
            L: list,
            U: list,
    ):

        """

        :param row: Current row of the coefficient matrix.
        :param column: Current column of the coefficient matrix.
        :param pivot_element: The pivot element of the current row.
        :param lower: The element below the pivot element.
        :param lowers: The row index of the lower element being eliminated.
        :param L: The lower matrix.
        :param U: The upper matrix.
        :return: Returns nothing.
        """

        row_operated_pivot: list = [coefficient * (lower / pivot_element) for coefficient in U[row]]
        L[lowers][column] = (lower / pivot_element)
        U[lowers] = [(lower_coeff - operated_element) for lower_coeff, operated_element
                     in zip(U[lowers], row_operated_pivot)]

    def solve(
            self,
            coefficient_matrix: list,
            constant_matrix: list
    ) -> tuple[list, list, list, list]:

        """

        :param coefficient_matrix: The coefficient matrix of type list of lists.
        :param constant_matrix: The constant matrix of type list of lists.
        :return: Returns the Lower triangular matrix 'L', upper triangular matrix 'U', intermediate roots 'Y', and final roots 'X'.
        """

        coefficient_matrix = coefficient_matrix.copy()
        constant_matrix = constant_matrix.copy()

        rows: int = len(coefficient_matrix)
        columns: int = len(coefficient_matrix[0])

        L = [[0 for _ in range(columns)] for _ in range(rows)]
        U = coefficient_matrix.copy()

        for row, column in zip(range(rows), range(columns)):

            L[row][row] = 1
            pivot_element = U[row][column]

            if pivot_element == 0.0:
                for lower_row in range(row + 1, rows):
                    temporary_pivot: int or float = U[lower_row][column]
                    if temporary_pivot != 0.0:
                        temporary_coefficient_row: list = U[row]
                        temporary_constant_row: list = constant_matrix[row]
                        U[row]: list = U[lower_row]
                        constant_matrix[row]: list = constant_matrix[lower_row]
                        U[lower_row]: list = temporary_coefficient_row
                        constant_matrix[lower_row]: list = temporary_constant_row

            if row != rows - 1:
                for lowers in range(row + 1, rows):
                    lower = U[lowers][column]
                    self.lower_eliminator(
                        row=row,
                        column=column,
                        pivot_element=pivot_element,
                        lower=lower,
                        lowers=lowers,
                        L=L,
                        U=U,
                    )

        Y = [0 for _ in range(rows)]
        Y[0] = constant_matrix[0][0]

        for row in range(rows - 1):
            for index in range(row + 1):
                constant_matrix[row + 1] = [constant_matrix[row + 1][0] - (L[row + 1][index] * Y[index])]
            Y[row + 1] = constant_matrix[row + 1][0]

        Y = [[constant] for constant in Y]

        U_copy = U.copy()
        Y_copy = Y.copy()

        for row in range(rows):
            pivot_element = U_copy[row][row]
            U_copy[row] = [coefficient * (1 / pivot_element) for coefficient in U_copy[row]]
            Y_copy[row] = [constant * (1 / pivot_element) for constant in Y_copy[row]]

        X = [0 for _ in range(rows)]
        X[-1] = Y_copy[-1][0]

        for row in range(rows - 1, 0, -1):
            for index in range(row, rows):
                Y_copy[row - 1] = [Y_copy[row - 1][0] - (U_copy[row - 1][index] * X[index])]
            X[row - 1] = Y_copy[row - 1][0]

        print(f"Lower Triangular Matrix:\n{L}\n")
        print(f"Upper Triangular Matrix:\n{U}\n")
        print(f"Intermediate Roots Y:\n{Y}\n")
        print(f"Final Roots X:\n{X}\n")

        return L, U, Y, X
