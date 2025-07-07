class TrapzoidalsRule:
    def __init__(self):
        # No initialization required
        ...

    def compute(self, step_size: float, function_values: list) -> float:
        # Applies the trapezoidal rule formula:
        # (h / 2) * [f(x0) + 2 * (f(x1) + f(x2) + ... + f(xn-1)) + f(xn)]
        starting_value, *middle_values, ending_value = function_values
        return (step_size / 2) * (starting_value + 2 * sum(middle_values) + ending_value)

    def solve(self, function: str, lower_limit: int, upper_limit: int, n: int) -> float:
        """
        Approximates the definite integral of a function using the Trapezoidal Rule.

        Parameters:
        function (str): The function to integrate as a string, e.g., "x**2 + 3".
                        The variable must be written as 'x'.
        lower_limit (int): The lower bound of integration.
        upper_limit (int): The upper bound of integration.
        n (int): The number of subintervals (must be a positive integer).

        Returns:
        float: Approximate integral value over the interval [lower_limit, upper_limit].
        """
        step_size = (upper_limit - lower_limit) / n
        x_values = [lower_limit]

        # Generate x values from lower_limit to upper_limit
        while len(x_values) != n + 1:
            lower_limit += step_size
            x_values.append(lower_limit)

        function_values = []
        for x in x_values:
            function_values.append(eval(function))  # Evaluate f(x) for each x

        return self.compute(step_size, function_values)
