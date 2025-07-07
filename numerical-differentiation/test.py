from backward_differentiation import BackwardDifferentiation
from forward_differentiation import ForwardDifferentiation

fwd_diff = ForwardDifferentiation()
bwd_diff = BackwardDifferentiation()

table = {1: 5, 2: 10, 3: 17, 4: 23, 5: 27, 6: 30}

print(f"Forward Difference 1st Order Derivative: {fwd_diff.solve(table, 2, order=1)}")
print(f"Forward Difference 2nd Order Derivative: {fwd_diff.solve(table, 1, order=2)}")
print(f"Backward Difference 3rd Order Derivative: {bwd_diff.solve(table, 6, 3)}")
