class SimpsonsThreeByEightRule:
    def __init__(self):
        # No initialization needed
        ...

    def compute(self, step_size: float, function_values: list) -> float:
        # Applies Simpson's 3/8 Rule:
        # (3h / 8) * [f(x0) + 3*(non-multiples of 3) + 2*(multiples of 3) + f(xn)]
        starting_value, *middle_values, ending_value = function_values
        non_multiples = [value for index, value in enumerate(middle_values) if (index + 1) % 3 != 0]
        multiples = [value for index, value in enumerate(middle_values) if (index + 1) % 3 == 0]
        return ((3 * step_size) / 8) * (starting_value + 3 * sum(non_multiples) + 2 * sum(multiples) + ending_value)

    def solve(self, function: str, lower_limit: int, upper_limit: int, n: int) -> float:
        """
        Approximates the definite integral of a function using Simpson's 3/8 Rule.

        Parameters:
        function (str): The function to integrate, provided as a string using 'x' as the variable.
        lower_limit (int): The starting point of the integration interval.
        upper_limit (int): The ending point of the integration interval.
        n (int): Number of subintervals (must be a multiple of 3 for exact rule compliance).

        Returns:
        float: Approximate integral value over [lower_limit, upper_limit].
        """
        step_size = (upper_limit - lower_limit) / n
        x_values = [lower_limit]

        # Generate all x values in the interval
        while len(x_values) != n + 1:
            lower_limit += step_size
            x_values.append(lower_limit)

        function_values = []
        for x in x_values:
            function_values.append(eval(function))  # Evaluate f(x) at each x

        return self.compute(step_size, function_values)
