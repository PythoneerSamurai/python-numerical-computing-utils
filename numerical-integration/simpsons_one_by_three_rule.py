class SimpsonsOneByThreeRule:
    def __init__(self):
        # No initialization required
        ...

    def compute(self, step_size: float, function_values: list) -> float:
        # Applies Simpson's 1/3 Rule:
        # (h / 3) * [f(x0) + 4 * (odd-indexed f(x)) + 2 * (even-indexed f(x)) + f(xn)]
        starting_value, *middle_values, ending_value = function_values
        odds = [value for index, value in enumerate(middle_values) if (index + 1) % 2 == 1]
        evens = [value for index, value in enumerate(middle_values) if (index + 1) % 2 == 0]
        return (step_size / 3) * (starting_value + 4 * sum(odds) + 2 * sum(evens) + ending_value)

    def solve(self, function: str, lower_limit: int, upper_limit: int, n: int) -> float:
        """
        Approximates the definite integral of a function using Simpson's 1/3 Rule.

        Parameters:
        function (str): Function to integrate, written as a string with 'x' as the variable (e.g., "x**2 + 1").
        lower_limit (int): Lower bound of integration.
        upper_limit (int): Upper bound of integration.
        n (int): Number of subintervals (must be even for exact rule compliance).

        Returns:
        float: Approximate integral over [lower_limit, upper_limit].
        """
        step_size = (upper_limit - lower_limit) / n
        x_values = [lower_limit]

        # Generate x values from a to b with n intervals
        while len(x_values) != n + 1:
            lower_limit += step_size
            x_values.append(lower_limit)

        function_values = []
        for x in x_values:
            function_values.append(eval(function))  # Evaluate f(x) for each x

        return self.compute(step_size, function_values)
