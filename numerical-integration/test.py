from simpsons_one_by_three_rule import SimpsonsOneByThreeRule
from simpsons_three_by_eight_rule import SimpsonsThreeByEightRule
from trapzoidals_rule import TrapzoidalsRule

function = "1 / (1 + x ** 2)"

trap = TrapzoidalsRule()
simp_obt = SimpsonsOneByThreeRule()
simp_tbe = SimpsonsThreeByEightRule()

print(f"Computed Integral using Trapzoidal's Rule: {trap.solve(function, 0, 2, 4)}")
print(f"Computed Integral using Simpsons One By Three Rule: {simp_obt.solve(function, 0, 2, 4)}")
print(f"Computed Integral using Simpsons Three By Eight Rule: {simp_tbe.solve(function, 0, 2, 4)}")
