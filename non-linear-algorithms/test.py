from bisection_method import BisectionMethod
from newton_raphson_method import NewtonRaphsonMethod
from regula_falsi_method import RegulaFalsiMethod
from regula_secant_method import RegulaSecantMethod
from fixed_point_iteration_method import FixedPointIterationMethod

from math import *

equation = "var ** 3 - 48"
differentiated_equation = "3 * var ** 2"
re_arranged_equation = "sqrt(48 / (var))"
re_arranged_equation_differentiated_equation = "(1/2) * (48 / var) ** (-3/2) * (-48 * var ** -2)"

print("---------- Bisection Method ----------\n")
BisectionMethod().solve(equation=equation, precision=2)
print("---------- Newton Raphson Method ----------\n")
NewtonRaphsonMethod().solve(
    equation=equation,
    differentiated_equation=differentiated_equation,
    precision=2,
)
print("---------- Regula Falsi Method ----------\n")
RegulaFalsiMethod().solve(equation=equation, precision=2)
print("---------- Regula Secant Method ----------\n")
RegulaSecantMethod().solve(equation=equation, precision=2)
print("---------- Fixed Point Iteration Method ----------\n")
FixedPointIterationMethod().solve(
    equation=equation,
    re_arranged_equation=re_arranged_equation,
    differentiated_equation=re_arranged_equation_differentiated_equation,
    precision=2,
)