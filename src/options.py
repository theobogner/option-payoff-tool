import numpy as np

def long_call(S, strike, premium):
    return np.maximum(S - strike, 0) - premium

def short_call(S, strike, premium):
    return premium - np.maximum(S - strike, 0)

def long_put(S, strike, premium):
    return np.maximum(strike - S, 0) - premium

def short_put(S, strike, premium):
    return premium - np.maximum(strike - S, 0)