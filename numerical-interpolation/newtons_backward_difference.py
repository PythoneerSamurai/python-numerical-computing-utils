import math
from collections import OrderedDict


class NewtonsBackwardDifference:

    def __init__(self):
        # Stores successive backward differences
        self.differences = []

    def difference_calculator(self, filtered_table_values: list):
        # Calculates one level of backward differences
        differences = []

        for index in range(len(filtered_table_values) - 1):
            # Subtract each value from the next
            differences.append(filtered_table_values[index + 1] - filtered_table_values[index])
        self.differences.append(differences)
        filtered_table_values = differences

        return filtered_table_values

    def solve(self, x_known: dict, x_unknown: int or float) -> float:
        """
        Estimates the value of a function at an unknown x using Newton's Backward Difference method.

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

        # Find xn (smallest x > x_unknown)
        xn = min([x for x in x_known.keys() if x > x_unknown])
        xn_index = list(x_known.keys()).index(xn)
        # Select values up to and including xn
        filtered_table_values = list(x_known.values())[:xn_index + 1]

        self.differences = []

        # Build backward difference table
        filtered_table_values = self.difference_calculator(filtered_table_values)
        while len(self.differences[-1]) != 1:
            filtered_table_values = self.difference_calculator(filtered_table_values)

        # Compute u = (x - xn) / h
        u = (x_unknown - xn) / (xn - list(x_known.keys())[xn_index - 1])
        fxn = list(x_known.values())[xn_index]

        # Apply Newton's Backward Difference formula
        for i in range(len(self.differences)):
            u_factor = u
            for j in range(i):
                u_factor *= (u + (j + 1))
            fxn += (u_factor / math.factorial(i + 1)) * self.differences[i][-1]

        return fxn
