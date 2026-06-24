import numpy as np
import matplotlib.pyplot as plt

from options import long_call

S = np.arange(50, 151, 1)

payoff = long_call(
    S,
    strike=100,
    premium=5
)

plt.plot(S, payoff)

plt.title("Long Call Payoff")
plt.xlabel("Underlying Price")
plt.ylabel("Profit / Loss")

plt.grid()

plt.show()