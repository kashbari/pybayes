from abc import ABC

class KalmanFilter(Estimator):
    def __init__(self, initial_state):