from newtons_forward_difference import NewtonsForwardDifference
from newtons_backward_difference import NewtonsBackwardDifference
from gauss_forward_central_difference import GaussForwardCentralDifference
from newtons_divided_difference import NewtonsDividedDifference
from lagrange_interpolation import LagrangeInterpolation

new_fwd_diff = NewtonsForwardDifference()
new_bwd_diff = NewtonsBackwardDifference()
gau_fwd_cen_diff = GaussForwardCentralDifference()
new_div_diff = NewtonsDividedDifference()
lag_interpol = LagrangeInterpolation()

fwd_diff_table = {1891: 46, 1901: 66, 1911: 81, 1921: 93, 1931: 101}
print(f"Newton's Forward Difference Result: {new_fwd_diff.solve(x_known=fwd_diff_table, x_unknown=1895)}")

bwd_diff_table = {0: 0, 0.5: 0.4794, 1.0: 0.8415, 1.5: 0.9975, 2.0: 0.9093}
print(f"Newton's Backward Difference Result: {new_bwd_diff.solve(x_known=bwd_diff_table, x_unknown=1.8)}")

gau_fwd_cen_diff_table = {1: 3, 2: 7, 3: 12, 4: 17, 5: 23}
print(f"Gauss Forward Central Difference Result: {gau_fwd_cen_diff.solve(x_known=gau_fwd_cen_diff_table, x_unknown=3.4)}")

div_diff_table = {3: 100, 4: 125, 5: 97, 7: 140, 8: 170, 10: 80}
print(f"Newton's Divided Difference Result: {new_div_diff.solve(x_known=div_diff_table, x_unknown=6)}")

lag_interpol_table = {1: 10, 3: 20, 4: 30, 6: 60}
print(f"Lagrange Interpolation Result: {lag_interpol.solve(lag_interpol_table, 3.75, unknown_type='output')}")

inv_lag_interpol_table = {2: 10, 4: 20, 5: 30, 7: 50}
print(f"Inverse Lagrange Interpolation Result: {lag_interpol.solve(inv_lag_interpol_table, 40, unknown_type='input')}")
