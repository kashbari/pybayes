from abc import ABC, abstractmethod
from itertools import product
from numpy import np


class Estimator(ABC):
    def __init__(self, initial_state, motion_model, observation_model, process_noise, measurement_noise):
        self.initial_state = initial_state
        self.motion_model = motion_model
        self.observation_model = observation_model
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        super().__init__()

    @abstractmethod
    def predict(self, time):
        return self.motion_model(new_time)

    @abstractmethod
    def update(self, new_measurement):
        pass
