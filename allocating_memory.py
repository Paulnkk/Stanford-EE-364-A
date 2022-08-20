import cvxpy as cp
import numpy as np
from allocate_memory_data import plot_memory
from allocate_memory_data import C,D,c,b
#Initializations and helper functions
m=256#number of banks
n=8#number of cores
M=cp.Variable((n,m),nonneg=True)
constraints=[M@np.ones((m,))==b,
M.T@np.ones((n,))<=c]
objective=cp.Minimize(cp.vec(M).T@cp.vec(C)+cp.vec(cp.power(M, 2))@cp.vec(D))
problem=cp.Problem(objective,constraints)
problem.solve()
plot_memory(M.value
