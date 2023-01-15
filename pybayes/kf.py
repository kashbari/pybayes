from abstract_estimator import Estimator
import numpy as np

class KalmanFilter(Estimator):
    '''
    Kalman Filter Implementation. Accomodates any various motion/observation models along with various process/measurement noises.
    Assumes linearity of motion motion. Linearization method available for EKF variant.
    '''
    def __init__(self, initial_state, motion_model, observation_model, process_noise, measurement_noise):
        pass