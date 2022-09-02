s_wc = sqrt(cvx_optval)
import cvxpy as cvx
import numpy as np

x = np.matrix(’0.1; 0.2; -0.05; 0.1’);
Sigma = cvx.semidefinite(4)

constraints =  [Sigma[0,0]==0.2, Sigma[1,1]==0.1]
constraints += [Sigma[2,2]==0.3, Sigma[3,3]==0.1]
constraints += [Sigma[0,1]>=0, Sigma[0,2]>=0]
constraints += [Sigma[1,2]<=0, Sigma[1,3]<=0, Sigma[2,3]>=0]
objective = cvx.Maximize(x.T*Sigma*x)

cvx.Problem(objective, constraints).solve()
sigma_wc = np.sqrt(objective.value)
