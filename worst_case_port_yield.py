import cvxpy as cp
from matplotlib import pyplot as plt
import numpy as np
import mosek
from worst_case_bond_price_data import y_nom, kappa, rho, c, T,t

delta = cp.Variable(T)
obj = c@cp.exp(cp.multiply(-t,(y_nom+delta)))
# obj = cp.sum([c[i]*cp.exp(-t[i]*(y_nom[i]+delta[i]))

# for i in range(T)])
constraints = [cp.sum(delta) == 0, delta[0]==0,cp.norm(delta,’inf’) <= kappa,cp.norm(cp.diff(delta)) <= rho]
prob = cp.Problem(cp.Minimize(obj),constraints)
prob.solve(solver=cp.MOSEK)
np.set_printoptions(suppress=True,precision=4)
# print(delta.value)
for con in constraints:
  print("\t",con.violation())
plt.plot(t,y_nom + delta.value,label="worst case")

plt.plot(t,y_nom,label="nominal")
plt.legend()
plt.xlabel("$t$")
plt.ylabel("yield")

print(f"The worst case value is {prob.value}.")
print(f"The nominal value is {c@(np.exp(-t*y_nom))}.")
