from abc import ABC, abstractmethod
from itertools import product
from numpy import np
import numpy.linalg as linalg
from numpy.linalg import cholesky as n_chol
from scipy.linalg import cholesky as s_chol

class Estimator(ABC):
    def __init__(self, initial_state, motion_model, observation_model, process_noise, measurement_noise, log):
        self.initial_state = initial_state
        self.motion_model = motion_model
        self.observation_model = observation_model
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        super().__init__()

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def update(self):
        pass

    def cholesky(self, x):
        return n_chol(x)