from collections import OrderedDict


class NewtonsDividedDifference:

    def __init__(self):
        # Stores successive divided differences
        self.differences = []

    def difference_calculator(self, table_inputs: list, table_values: list, step_size: int):
        # Calculates one level of divided differences
        differences = []

        for index in range(len(table_values) - 1):
            # Compute the divided difference using increasing step size
            difference = ((table_values[index + 1] - table_values[index])
                          / (table_inputs[index + step_size] - table_inputs[index]))
            differences.append(difference)
        self.differences.append(differences)
        table_values = differences

        return table_values

    def solve(self, x_known: dict, x_unknown: int or float) -> float:
        """
        Estimates the value of a function at an unknown x using Newton's Divided Difference method.

        Parameters:
        x_known (dict): A dictionary of known x and corresponding f(x) values.
                        x-values do not need to be uniformly spaced.
        x_unknown (int or float): The x-value at which f(x) is to be estimated.

        Returns:
        float: Estimated f(x) at x_unknown.
        """
        # Ensure x_unknown lies within the known x range
        assert max(x_known.keys()) > x_unknown > min(x_known.keys())
        # Sort the known x-values
        x_known = OrderedDict(sorted(x_known.items()))

        table_inputs = list(x_known.keys())
        table_values = list(x_known.values())

        step_size = 1
        self.differences = []

        # Build the divided difference table
        table_values = self.difference_calculator(table_inputs, table_values, step_size)
        while len(self.differences[-1]) != 1:
            step_size += 1
            table_values = self.difference_calculator(table_inputs, table_values, step_size)

        fxn = list(x_known.values())[0]

        # Apply Newton's Divided Difference formula
        multiplicative_history = 1
        for i in range(len(self.differences)):
            multiplicative_factor = multiplicative_history * (x_unknown - table_inputs[i])
            multiplicative_history = multiplicative_factor
            fxn += multiplicative_factor * self.differences[i][0]

        return fxn
