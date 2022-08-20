import numpy as np
import cvxpy as cp
from late_reporting_time_series_data import *

ell = cp.Variable(N,nonneg=True)

y = cp.Variable(N,nonneg=True)

obj = cp.sum_squares(cp.diff(y,2))

constraints = [cp.sum(ell) <= .1*cp.sum(y), ell <= y]
constraints += [y_tilde[0] == y[0]-ell[0], y_tilde[1:-1] == y[1:-1]-ell[1:-1]+ell[:-2], y_tilde[-1] == y[-1]+ell[-2]]

prob = cp.Problem(cp.Minimize(obj),constraints)
prob.solve(solver=cp.ECOS)

print(f"The optimal objective is {obj.value}")
y_rec = y.value

RMS = ((y_rec-y_true)**2).mean()**.5
print(f"The RMS between the recovered and true time series is {RMS}.")
RMS = ((y_tilde-y_true)**2).mean()**.5
print(f"The RMS between the observed and true time series is {RMS}.")
plot_helper(y_rec)
