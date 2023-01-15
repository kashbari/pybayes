from abstract_estimator import Estimator
import numpy as np
import numpy.linalg as linalg
from numpy.linalg import cholesky as n_chol
from scipy.linalg import cholesky as s_chol

class UnscentedKalmanFilter(Estimator):
    '''
    Unscented Kalman Filter Implementation. Computation of Sigma Points included along with square root variant.
    '''
    def __init__(self, initial_state, motion_model, observation_model, process_noise, measurement_noise, square_root=True):
        pass

    def sigma_points(self):
        pass

    def cholesky(self, x):
        return n_chol(x)