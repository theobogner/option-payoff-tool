import numpy as np
import matplotlib.pyplot as plt

from options import (
    long_call,
    long_put,
    short_call,
    short_put
)

from strategies import (
    straddle,
    strangle,
    bull_call_spread,
    bear_put_spread,
    butterfly
)

S = np.arange(50, 151, 1)

strategy = "butterfly"  # Change this to test different strategies

# Long Call
if strategy == "long_call":
    payoff = long_call(S, 100, 5)

# Long Put
elif strategy == "long_put":
    payoff = long_put(S, 100, 5)

# Short Call
elif strategy == "short_call":
    payoff = short_call(S, 100, 5)

# Short Put
elif strategy == "short_put":
    payoff = short_put(S, 100, 5)

# Long Call(K1) + Long Put(K1)
elif strategy == "straddle":
    payoff = straddle(
        S,
        k1=100,
        prem1=5,
        prem2=4
    )

# Long Put(K1) + Long Call(K2)
elif strategy == "strangle":
    payoff = strangle(
        S,
        k1=90,
        k2=110,
        prem1=3,
        prem2=3
    )

# Long Call(K1) + Short Call(K2)
elif strategy == "bull_call_spread":
    payoff = bull_call_spread(
        S,
        k1=100,
        k2=120,
        prem1=5,
        prem2=2
    )

# Long Put(K2) + Short Put(K1)
elif strategy == "bear_put_spread":
    payoff = bear_put_spread(
        S,
        k1=120,
        k2=100,
        prem1=7,
        prem2=3
    )

# Long Call(K1) - 2 Long Call(K2) + Long Call(K3)
elif strategy == "butterfly":
    payoff = butterfly(
        S,
        k1=90,
        k2=100,
        k3=110,
        prem1=6,
        prem2=4,
        prem3=2
    )

else:
    raise ValueError(f"Unknown strategy: {strategy}")

plt.plot(S, payoff)

plt.axhline(0, color="black")

plt.title(strategy.replace("_", " ").title())
plt.xlabel("Underlying Price")
plt.ylabel("Profit / Loss")

plt.grid()
plt.show()