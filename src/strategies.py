from options import (
    long_call,
    short_call,
    long_put,
    short_put
)


def straddle(S, k1, prem1, prem2):
    return (
        long_call(S, k1, prem1)
        + long_put(S, k1, prem2)
    )


def strangle(S, k1, k2, prem1, prem2):
    return (
        long_put(S, k1, prem1)
        + long_call(S, k2, prem2)
    )


def bull_call_spread(S, k1, k2, prem1, prem2):
    return (
        long_call(S, k1, prem1)
        + short_call(S, k2, prem2)
    )


def bear_put_spread(S, k1, k2, prem1, prem2):
    return (
        long_put(S, k2, prem2)
        + short_put(S, k1, prem1)
    )


def butterfly(S, k1, k2, k3, prem1, prem2, prem3):
    return (
        long_call(S, k1, prem1)
        - 2 * long_call(S, k2, prem2)
        + long_call(S, k3, prem3)
    )