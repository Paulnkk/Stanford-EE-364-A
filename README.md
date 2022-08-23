# CVXPY-backtesting-implementations

Backtesting framework for solving several convex optimization problems. These problems were solved for commercial purposes on a large scale basis (basic problems with 'low' dimensional data provided in this repo). Even though those frameworks could be used to efficiently solve the problems for high dimensional datasets. 

-> energy_storage_trade_off.ipynb is solving the convex optimization problem of charging a Lithium-Ion-battery under capactiy constraints.

-> risk-return-portfolios-with-loss-constraint.ipynb is solving a portfolio Optimization problem (Markowitz-approach) under normally distributed probability constraints.

-> allocating_memory.py is solving a multicore processor problem with n cores and m memory blocks.

-> recover_ts.py the corrupted time series y^tilde but not the true one y. The goal is to find an estimate y^hat of the true time series y, which we do by minimizing a convex loss function.

-> sparse_matrix.py estimating a sparse covariance matrix based on normally distributed datapoints (stanadrized) by minimizing negative log-likelihood


------------> formulation of the the Optimization problems (Latex) will be added to the repo in future 
