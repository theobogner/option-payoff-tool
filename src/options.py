import numpy as np

def long_call(S, strike, premium):
    return np.maximum(S - strike, 0) - premium