import itertools


class GaussEliminationMethod:
    def __init__(self):
        # Empty Constructor function, nothing to initialize.
        pass

    def lower_eliminator(
            self,
            row: int,
            lower: int or float,
            lowers: int,
            coefficient_matrix: list,
            constant_matrix: list,
    ):

        """

        :param row: Current row of the coefficient matrix.
        :param lower: The element below the pivot element.
        :param lowers: The row index of the lower element being eliminated.
        :param coefficient_matrix: The coefficient matrix of type list of lists.
        :param constant_matrix: The constant matrix of type list of lists.
        :return: Returns nothing.
        """

        row_operated_pivot: list = [coefficient * lower for coefficient in coefficient_matrix[row]]
        coefficient_matrix[lowers] = [(lower_coeff - operated_element) for lower_coeff, operated_element
                                      in zip(coefficient_matrix[lowers], row_operated_pivot)]
        row_operated_constant: int or float = constant_matrix[row][0] * lower
        constant_matrix[lowers] = [(lower_constant - row_operated_constant) for lower_constant
                                   in constant_matrix[lowers]]

    def solve(
            self,
            coefficient_matrix: list,
            constant_matrix: list
    ) -> list:

        """

        :param coefficient_matrix: The coefficient matrix of type list of lists.
        :param constant_matrix: The constant matrix of type list of lists.
        :return: Returns the computed roots of the given coefficient matrix.
        """

        coefficient_matrix = coefficient_matrix.copy()
        constant_matrix = constant_matrix.copy()

        rows: int = len(coefficient_matrix)
        columns: int = len(coefficient_matrix[0])

        for row, column in zip(range(rows), range(columns)):

            pivot_element: int or float = coefficient_matrix[row][column]

            if pivot_element == 0.0:
                for lower_row in range(row + 1, rows):
                    temporary_pivot = coefficient_matrix[lower_row][column]
                    if temporary_pivot != 0.0:
                        temporary_coefficient_row = coefficient_matrix[row]
                        temporary_constant_row = constant_matrix[row]
                        coefficient_matrix[row] = coefficient_matrix[lower_row]
                        constant_matrix[row] = constant_matrix[lower_row]
                        coefficient_matrix[lower_row] = temporary_coefficient_row
                        constant_matrix[lower_row] = temporary_constant_row

            coefficient_matrix[row] = [coefficient * (1 / pivot_element) for coefficient in coefficient_matrix[row]]
            constant_matrix[row] = [constant * (1 / pivot_element) for constant in constant_matrix[row]]

            if row != rows - 1:
                for lowers in range(row + 1, rows):
                    lower: int or float = coefficient_matrix[lowers][column]
                    self.lower_eliminator(
                        row=row,
                        lower=lower,
                        lowers=lowers,
                        coefficient_matrix=coefficient_matrix,
                        constant_matrix=constant_matrix
                    )

        for row in range(rows - 1, 0, -1):
            for index in range(row, rows):
                constant_matrix[row - 1] = [
                    constant_matrix[row - 1][0] - (coefficient_matrix[row - 1][index] * constant_matrix[index][0])
                ]

        constant_matrix = list(itertools.chain.from_iterable(constant_matrix))
        print("\nRoots:\n")
        [print(f"x{index + 1}:{constant}\n") for index, constant in enumerate(constant_matrix)]

        return constant_matrix
