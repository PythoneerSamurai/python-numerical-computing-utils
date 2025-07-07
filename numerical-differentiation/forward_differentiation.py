from collections import OrderedDict


class ForwardDifferentiation:

    def __init__(self):
        # Stores forward difference table
        self.differences = []

    def difference_calculator(self, filtered_table_values: list):
        # Computes one level of forward differences
        differences = []

        for index in range(len(filtered_table_values) - 1):
            differences.append(filtered_table_values[index + 1] - filtered_table_values[index])
        self.differences.append(differences)
        filtered_table_values = differences

        return filtered_table_values

    def first_order_differentiation(self, step_size: int | float) -> float:
        # Computes the first derivative using forward difference approximation
        diff = 0
        for index, difference in enumerate(self.differences):
            if index % 2 == 0:
                diff += (1 / (index + 1)) * difference[0]
            else:
                diff -= (1 / (index + 1)) * difference[0]
        return diff / step_size

    def second_order_differentiation(self, step_size: int | float) -> float:
        # Computes the second derivative using a weighted forward difference series
        diff = 0
        fractional_coefficient = 11 / 12
        coefficient_decrease_factor = fractional_coefficient - (5 / 6)
        for index, difference in enumerate(self.differences[1:]):
            if index == 0:
                diff += difference[0]
            elif index == 1:
                diff -= difference[0]
            else:
                if index % 2 == 0:
                    diff += fractional_coefficient * difference[0]
                    fractional_coefficient -= coefficient_decrease_factor
                else:
                    diff -= fractional_coefficient * difference[0]
                    fractional_coefficient -= coefficient_decrease_factor
        return diff / step_size ** 2

    def third_order_differentiation(self, step_size: int | float) -> float:
        # Computes the third derivative using a weighted forward difference series
        diff = 0
        fractional_coefficient = 3 / 2
        coefficient_decrease_factor = fractional_coefficient - (7 / 5)
        for index, difference in enumerate(self.differences[2:]):
            if index == 0:
                diff += difference[0]
            else:
                if index % 2 == 0:
                    diff += fractional_coefficient * difference[0]
                    fractional_coefficient -= coefficient_decrease_factor
                else:
                    diff -= fractional_coefficient * difference[0]
                    fractional_coefficient -= coefficient_decrease_factor
        return diff / step_size ** 3

    def solve(self, x_known: dict, x_diff: int | float, order: int) -> float | None:
        """
        Computes the first, second, or third derivative at a point using Newton's Forward Difference method.

        Parameters:
        x_known (dict): Dictionary of known x and f(x) values. Must be uniformly spaced.
        x_diff (int | float): The x-value at which the derivative is to be computed.
                              Must not be the last x-value in the table.
        order (int): The order of the derivative (1 for first, 2 for second, 3 for third).

        Returns:
        float | None: The computed derivative value, or None for an invalid order.
        """
        x_known = OrderedDict(sorted(x_known.items()))
        assert x_diff != list(x_known.keys())[-1]  # Cannot compute at the last x-value (no forward data)

        x_diff_index = list(x_known.keys()).index(x_diff)
        filtered_table_values = list(x_known.values())[x_diff_index:]

        # Build forward difference table
        self.differences = []
        filtered_table_values = self.difference_calculator(filtered_table_values)
        while len(self.differences[-1]) != 1:
            filtered_table_values = self.difference_calculator(filtered_table_values)

        step_size = list(x_known.keys())[1] - list(x_known.keys())[0]

        if order == 1:
            return self.first_order_differentiation(step_size)
        elif order == 2:
            return self.second_order_differentiation(step_size)
        elif order == 3:
            return self.third_order_differentiation(step_size)
        else:
            print("Derivatives can be computed upto third order, please enter a valid order (1 to 3).")
            return None
