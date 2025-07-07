import math
from collections import OrderedDict


class GaussForwardCentralDifference:

    def __init__(self):
        # Stores successive central differences
        self.differences = []

    def difference_calculator(self, table_values: list):
        # Calculates one level of forward differences
        differences = []

        for index in range(len(table_values) - 1):
            # Subtract each value from the next
            differences.append(table_values[index + 1] - table_values[index])
        self.differences.append(differences)
        table_values = differences

        return table_values

    def solve(self, x_known: dict, x_unknown: int or float) -> float:
        """
        Estimates the value of a function at an unknown x using Gauss's Forward Central Difference method.

        Parameters:
        x_known (dict): A dictionary of known x and corresponding f(x) values.
                        Must be uniformly spaced and centered around the target x.
        x_unknown (int or float): The x-value at which f(x) is to be estimated.

        Returns:
        float: Estimated f(x) at x_unknown.
        """
        # Ensure x_unknown is within bounds
        assert max(x_known.keys()) > x_unknown > min(x_known.keys())
        # Sort known x-values
        x_known = OrderedDict(sorted(x_known.items()))
        total_given_x_values = len(x_known.keys())

        # Find the central x-value index
        central_x_value = math.ceil(total_given_x_values / 2) - 1
        x0_index = central_x_value if total_given_x_values % 2 == 1 else central_x_value + 1
        x0 = list(x_known.keys())[x0_index]

        table_values = list(x_known.values())

        # Build central difference table
        self.differences = []
        table_values = self.difference_calculator(table_values)
        while len(self.differences[-1]) != 1:
            table_values = self.difference_calculator(table_values)

        # Compute u = (x - x0) / h
        u = (x_unknown - x0) / (list(x_known.keys())[x0_index + 1] - x0)
        u_factor_list = []

        # Generate list of (u ± n) terms used in the product series
        for num in range(1, len(self.differences) - 1):
            u_factor_list.append((u - num))
            u_factor_list.append((u + num))
        u_factor_list.pop(-1)  # Remove extra term

        fxn = list(x_known.values())[x0_index]

        # Apply Gauss Forward Central Difference formula
        for i in range(len(self.differences)):
            u_factor = u

            for j in range(i):
                u_factor *= u_factor_list[j]

            total_difference_values = len(self.differences[i])
            difference_factor = math.ceil(total_difference_values / 2) - 1
            central_difference_index = difference_factor if total_difference_values % 2 == 1 else difference_factor + 1

            fxn += (u_factor / math.factorial(i + 1)) * self.differences[i][central_difference_index]

        return fxn
