from math import *

class NewtonRaphsonMethod:
    def __init__(self):
        # Empty constructor function, nothing to initialize.
        pass

    def function(self, equation: str, value: int or float) -> float:
        """

        :param equation: The string equation to be evaluated. The variable present in the equation must be named "var".
        :param value: The value to substitute in the equation.
        :return: Returns the result of the equation.
        """
        var: int or float = value
        return eval(equation)

    def derivative(self, equation: str, value: int or float) -> float:
        """

        :param equation: The derivative of the string equation, the variable must be named "var".
        :param value: The value to substitute in the equation.
        :return: The result of the equation.
        """
        var: int or float = value
        return eval(equation)

    def a_b_locator(
            self,
            range_lower_limit: int,
            range_upper_limit: int,
            equation: str
    ) -> tuple[int, int] or None:
        """

        :param range_lower_limit: The lower bound of the range of the real line.
        :param range_upper_limit: The upper bound of the range of the real line.
        :param equation: The string equation to be evaluated, the variable must be named "var".
        :return: Returns the roots 'a and b' that satisfy "f(a)*f(b) < 0".
        """

        real_line: list = [
            value / 2.0 for value in
            range(range_lower_limit, range_upper_limit, 1)
        ]
        real_numbers_to_values: dict = {index: self.function(equation, index) for index in real_line}
        real_numbers: list = list(real_numbers_to_values.keys())
        real_number_function_values: list = list(real_numbers_to_values.values())

        a_b_products_dict: dict = {}

        for index in range(len(real_number_function_values) - 1):
            for greater_index in range(index + 1, len(real_number_function_values) - 1):
                key: tuple = (index, greater_index)
                value: float = (real_number_function_values[index] * real_number_function_values[greater_index])
                a_b_products_dict[key] = value

        a_b_product_keys: list = list(a_b_products_dict.keys())
        a_b_product_values: list = list(a_b_products_dict.values())

        try:
            min_negative_products: list = [index for index in a_b_product_values if index < 0]
            assert len(min_negative_products) != 0
            closest_to_zero_product_index: int = a_b_product_values.index(max(min_negative_products))
            a_index, b_index = a_b_product_keys[closest_to_zero_product_index]

            a: int
            b: int

            a, b = real_numbers[int(a_index)], real_numbers[int(b_index)]

            return a, b

        except AssertionError:
            print(
                "None of the roots in the real line satisfy the condition f(a)*f(b) < 0, please broaden the real line."
            )

    def solve(self,
              equation: str,
              differentiated_equation: str,
              iterations: int=20,
              range_lower_limit: int=-10,
              range_upper_limit: int=10,
              precision: int=2
              ) -> float or None:
        """

        :param equation: The string equation to be evaluated. The variable must be named "var".
        :param differentiated_equation: The differentiated string equation. The variable must be named "var".
        :param iterations: The number of iterations to run.
        :param range_lower_limit: The lower bound of the range of the real line.
        :param range_upper_limit: The upper bound of the range of the real line.
        :param precision: The precision to be used as a stopping criterion.
        :return: Returns the root of the equation if computed, else None.
        """

        a, b = self.a_b_locator(
            range_lower_limit, range_upper_limit, equation
        )
        print(f"The roots that satisfy f(a).f(b)<0 are: a = {a}, b = {b}")

        x_n = round((a + b) / 2, precision)

        for iteration in range(iterations):

            x_history: float = x_n

            function_value: float = self.function(equation, x_n)
            derivative_value: float = self.derivative(differentiated_equation, x_n)

            print(
                f"Iteration {iteration}:\n  x_{iteration}: {x_n: .{precision}f}, function_value: {function_value: .{precision}f}, derivative_value: {derivative_value: .{precision}f}"
            )

            x_n: float = x_n - (function_value / derivative_value)
            x_n: int or float = round(x_n, precision)

            if x_history == x_n:
                print(f"\nRequired Root: {x_n: .{precision}f}")
                return x_n

        print("""Root could not be approximated with the specified number of iterations, for the desired precision level.
        Consider increasing the number of iterations or decreasing the precision level.""")
        return None

