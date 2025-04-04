import itertools


class GaussSeidelIterativeMethod():
    def __init__(self):
        # Empty Constructor function, nothing to initialize.
        pass

    def former_handler(
            self,
            row: int,
            roots: list,
            placeholder_values: list,
            former: int or float,
            formers: int,
    ):

        """

        :param row: Current row of the coefficient matrix.
        :param roots: Current roots of the coefficient matrix.
        :param placeholder_values: Intermediate roots of the coefficient matrix.
        :param former: The element before the pivot element.
        :param formers: The column index of the former element.
        :return: Returns nothing.
        """

        operated_former: int or float = former * roots[formers]
        placeholder_values[row]: list = placeholder_values[row] - operated_former
        roots[row]: list = placeholder_values[row]

    def latter_handler(
            self,
            row: int,
            roots: list,
            placeholder_values: list,
            latter: int or float,
            latters: int,
    ):

        """

        :param row: Current row of the coefficient matrix.
        :param roots: Current roots of the coefficient matrix.
        :param placeholder_values: Intermediate roots of the coefficient matrix.
        :param latter: The element after the pivot element.
        :param latters: The column index of the latter element.
        :return: Returns nothing.
        """

        operated_latter: int or float = latter * roots[latters]
        placeholder_values[row]: list = placeholder_values[row] - operated_latter
        roots[row]: list = placeholder_values[row]

    def iterator(
            self,
            rows: int,
            columns: int,
            iteration: int,
            roots: list,
            placeholder_values: list,
            coefficient_matrix: list,
            constant_matrix: list,
            placeholder_coefficient_matrix: list,
    ) -> list:

        """

        :param rows: The number of rows in the coefficient matrix.
        :param columns: The number of columns in the coefficient matrix.
        :param iteration: The current iteration.
        :param roots: The current roots of the coefficient matrix.
        :param placeholder_values: The intermediate roots of the coefficient matrix.
        :param coefficient_matrix: The coefficient matrix.
        :param constant_matrix: The constant matrix.
        :param placeholder_coefficient_matrix: A temporary copy of the coefficient matrix.
        :return: Returns the roots after the current iteration.
        """

        for row, column in zip(range(rows), range(columns)):
            pivot_element: int or float = placeholder_coefficient_matrix[row][column]

            if pivot_element == 0.0:
                for lower_row in range(row + 1, rows):
                    temporary_pivot: int or float = coefficient_matrix[lower_row][column]
                    if temporary_pivot != 0.0:
                        temporary_coefficient_row: list = coefficient_matrix[row]
                        temporary_constant_row: list = constant_matrix[row]
                        coefficient_matrix[row]: list = coefficient_matrix[lower_row]
                        constant_matrix[row]: list = constant_matrix[lower_row]
                        coefficient_matrix[lower_row]: list = temporary_coefficient_row
                        constant_matrix[lower_row]: list = temporary_constant_row

            if iteration == 0:
                coefficient_matrix[row] = [coefficient * (1 / pivot_element) for coefficient in coefficient_matrix[row]]

            placeholder_values[row] = placeholder_values[row] * (1 / pivot_element)

            if row == 0:
                for latters in range(1, columns):
                    latter: int or float = coefficient_matrix[row][latters]
                    self.latter_handler(
                        row=row,
                        roots=roots,
                        placeholder_values=placeholder_values,
                        latter=latter,
                        latters=latters,
                    )

            elif row == rows - 1:
                for formers in range(0, columns - 1):
                    former: int or float = coefficient_matrix[row][formers]
                    self.former_handler(
                        row=row,
                        roots=roots,
                        placeholder_values=placeholder_values,
                        former=former,
                        formers=formers,
                    )

            else:
                for formers in range(0, column):
                    former: int or float = coefficient_matrix[row][formers]
                    self.former_handler(
                        row=row,
                        roots=roots,
                        placeholder_values=placeholder_values,
                        former=former,
                        formers=formers,
                    )

                for latters in range(column + 1, columns):
                    latter: int or float = coefficient_matrix[row][latters]
                    self.latter_handler(
                        row=row,
                        roots=roots,
                        placeholder_values=placeholder_values,
                        latter=latter,
                        latters=latters,
                    )

        return placeholder_values.copy()

    def solve(
            self,
            iterations: int,
            coefficient_matrix: list,
            constant_matrix: list
    ) -> list:

        """

        :param iterations: The total number of iterations.
        :param coefficient_matrix: The coefficient matrix.
        :param constant_matrix: The constant matrix.
        :return: The computed roots of the given coefficient matrix.
        """

        rows: int = len(coefficient_matrix)
        columns: int = len(coefficient_matrix[0])
        roots = [0 for _ in range(columns)]
        placeholder_coefficient_matrix = coefficient_matrix.copy()

        for iteration in range(iterations):
            placeholder_values = list(itertools.chain.from_iterable(constant_matrix.copy()))
            roots = self.iterator(
                rows=rows,
                columns=columns,
                iteration=iteration,
                roots=roots,
                placeholder_values=placeholder_values,
                coefficient_matrix=coefficient_matrix,
                constant_matrix=constant_matrix,
                placeholder_coefficient_matrix=placeholder_coefficient_matrix
            )

            print(f"\nIteration: {iteration}:\n")
            [print(f"x{index + 1}:{constant}\n") for index, constant in enumerate(roots)]

        return roots
