from collections import OrderedDict


class LagrangeInterpolation:
    def __init__(self):
        # No initialization needed
        ...

    def input_finder(self, inputs: list, outputs: list, unknown: int or float):
        # Estimates the input value for a given output using Lagrange interpolation
        calculations = []
        for index, output in enumerate(outputs):
            calculation = 1
            # Copy the outputs and exclude the current one
            others = outputs.copy()
            others.remove(output)
            for other in others:
                # Construct Lagrange basis polynomial for input estimation
                calculation *= (unknown - other) / (output - other)
            calculation *= inputs[index]
            calculations.append(calculation)
        return sum(calculations)

    def output_finder(self, inputs: list, outputs: list, unknown: int or float) -> float:
        # Estimates the output value for a given input using Lagrange interpolation
        calculations = []
        for index, input in enumerate(inputs):
            calculation = 1
            # Copy the inputs and exclude the current one
            others = inputs.copy()
            others.remove(input)
            for other in others:
                # Construct Lagrange basis polynomial for output estimation
                calculation *= (unknown - other) / (input - other)
            calculation *= outputs[index]
            calculations.append(calculation)
        return sum(calculations)

    def solve(self, known: dict, unknown: int or float, unknown_type: str) -> float | None:
        """
        Estimates either input or output using Lagrange interpolation.

        Parameters:
        known (dict): Dictionary of known input-output pairs.
        unknown (int or float): The value to estimate (input or output).
        unknown_type (str): Specify whether the unknown is 'input' or 'output'.

        Returns:
        float | None: Estimated value, or None if unknown_type is invalid.
        """
        # Sort known data
        known = OrderedDict(sorted(known.items()))

        inputs = list(known.keys())
        outputs = list(known.values())

        if unknown_type.lower() == "input":
            # Ensure unknown output lies in the range
            assert max(known.values()) > unknown > min(known.values())
            return self.input_finder(inputs, outputs, unknown)
        elif unknown_type.lower() == "output":
            # Ensure unknown input lies in the range
            assert max(known.keys()) > unknown > min(known.keys())
            return self.output_finder(inputs, outputs, unknown)
        else:
            # Handle invalid type
            print("The unknown type can either be 'input' or 'output'. Please enter a valid type.")
            return None
