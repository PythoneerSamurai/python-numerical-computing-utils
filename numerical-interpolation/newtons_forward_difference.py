import math
from collections import OrderedDict


class NewtonsForwardDifference:
    def __init__(self):
        # Stores successive forward differences
        self.differences = []

    def difference_calculator(self, filtered_table_values: list):
        # Calculates one level of forward differences
        differences = []

        for index in range(len(filtered_table_values) - 1):
            # Subtract each value from the next
            differences.append(filtered_table_values[index + 1] - filtered_table_values[index])
        self.differences.append(differences)
        filtered_table_values = differences

        return filtered_table_values

    def solve(self, x_known: dict, x_unknown: int or float) -> float:
        """
        Estimates the value of a function at an unknown x using Newton's Forward Difference method.

        Parameters:
        x_known (dict): A dictionary of known x and corresponding f(x) values.
                        Must be uniformly spaced.
        x_unknown (int or float): The x-value at which f(x) is to be estimated.

        Returns:
        float: Estimated f(x) at x_unknown.
        """
        # Ensure x_unknown is within bounds
        assert max(x_known.keys()) > x_unknown > min(x_known.keys())
        # Sort known x-values
        x_known = OrderedDict(sorted(x_known.items()))

        # Find x0 (largest x < x_unknown)
        x0 = max([x for x in x_known.keys() if x < x_unknown])
        x0_index = list(x_known.keys()).index(x0)
        # Select values from x0 onwards
        filtered_table_values = list(x_known.values())[x0_index:]

        # Build difference table
        self.differences = []
        filtered_table_values = self.difference_calculator(filtered_table_values)
        while len(self.differences[-1]) != 1:
            filtered_table_values = self.difference_calculator(filtered_table_values)

        # Compute u = (x - x0) / h
        u = (x_unknown - x0) / (list(x_known.keys())[x0_index + 1] - x0)
        fxn = list(x_known.values())[x0_index]

        # Apply Newton's Forward Difference formula
        for i in range(len(self.differences)):
            u_factor = u
            for j in range(i):
                u_factor *= (u - (j + 1))
            fxn += (u_factor / math.factorial(i + 1)) * self.differences[i][0]

        return fxn
