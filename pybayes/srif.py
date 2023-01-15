from abstract_estimator import Estimator
import numpy as np
import numpy.linalg as linalg
from numpy.linalg import cholesky as n_chol
from scipy.linalg import cholesky as s_chol

class SquareRootInformationFilter(Estimator):
    '''
    Square Root Information Filter Implementation
    '''
    def __init__(self, initial_state, motion_model, observation_model, process_noise, measurement_noise):
        pass