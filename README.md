# CVXPY-backtesting-implementations

Notebook with example from convex optimization. All problems are implemented and solved with cvxpy.

-> energy_storage_trade_off.ipynb is solving the convex optimization problem of charging a Lithium-Ion-battery under capactiy constraints.

-> risk-return-portfolios-with-loss-constraint.ipynb is solving a portfolio Optimization problem (Markowitz-approach) under normally distributed probability constraints.

-> allocating_memory.py is solving a multicore processor problem with n cores and m memory blocks.

-> recover_ts.py the corrupted time series y^tilde but not the true one y. The goal is to find an estimate y^hat of the true time series y, which we do by minimizing a convex loss function.

-> sparse_matrix.py estimating a sparse covariance matrix based on normally distributed datapoints (standardized) by minimizing negative log-likelihood.

-> worst_case_port_yield.py generates yield curves for worst case and nominal case bond portfolio optimization (worst_case_bond_price_data data required for execution), under the assumption that the set which consists of all yield curves is convex.

-> bounding_port_risk.py max risk under constraints for the covariance matrix and create worst case portfolio

-> LDA_gauss linear classifier for datapoints extracted from normal-distributed data source using 5 clusters with center mu_i


---> formulation of the the Optimization problems (Latex) will be added to the repo in future 
