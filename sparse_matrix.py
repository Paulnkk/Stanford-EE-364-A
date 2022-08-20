
import numpy as np
import cvxpy as cp
from matplotlib import pyplot as plt
from estim_sparse_cov_data import X, Sigma_true, lam, Sigma_emp, plot_helper

def solve_iterate(X, S_, lam):
  d, _ = S_.shape
  Z = cp.Variable((d, d), PSD=True)
  n = X.shape[0]
  
  Sinv = np.linalg.inv(S_)
  obj = cp.log_det(S_)+cp.trace(Sinv@(Z-S_)) + \
    cp.matrix_frac(X.T/n**.5, Z)+lam*cp.norm(cp.upper_tri(Z), 1)
  
  prob = cp.Problem(cp.Minimize(obj))
  prob.solve()

  
def solve_ccp(X, init, lam):
  obs = []
  Z = init.copy()
  
  for i in range(10):
    Z, val = solve_iterate(X, Z, lam=lam)
    obs.append(val)
    
return Z, obs

if __name__ == "__main__":
  
  Z, obs = solve_ccp(X, init=Sigma_emp, lam=lam)
  plt.plot(obs, label="emp. init.")
  _, obs2 = solve_ccp(X, init=np.eye(Sigma_true.shape[0]), lam=lam)
  
  plt.plot(obs2, label="Id. init.")
  plt.legend()
  save_dest = "files/figures/estim_sparse_cov_obj.pdf"
  
  plt.ylabel("Objective")
  plt.tight_layout()
  plt.savefig(save_dest, bbox_inches=’tight’)
  
  save_dest = "files/figures/estim_sparse_cov.pdf"
  plot_helper(Z, save_dest)
  from estim_sparse_cov_data import Sigma_true,Sigma_emp
  err_est = np.abs(Sigma_true-Z).sum()
  print("The L1 error between the true Sigma and the estimate is: ", err_est)err_emp = np.abs(Sigma_true-Sigma_emp).sum()
print("The L1 error between the true Sigma and the empirical is: ", err_emp# print(Sigma_emp)
