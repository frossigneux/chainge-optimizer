# /usr/bin/env python3

import defi.defi_tools as dft
import matplotlib.pyplot as plt

import numpy as np


chng_price = 0.11
chng_pool_apr = 167  # 430

targets = [
    0.2,
    0.4,
    0.6,
    0.8,
    1.0,
    1.2,
    1.4,
    1.6,
    1.8,
    2.0,
]

performances = []
for duration in [30, 60, 180, 365]:
    for target in targets:
        result = dft.compare(
            days=duration,
            var_A=0,
            var_B=target / chng_price * 100,
            rw_pool_A=0,
            rw_pool_B=0,
            rw_pool_AB=chng_pool_apr / 365,
            fees_AB=0,
        )
        performances.append(float(result["farm"][:-1]) / float(result["buy_hold"][:-1]))


labels = []
for duration in [30, 60, 180, 365]:
    for target in targets:
        labels.append(f"{target}$")

x = np.arange(len(labels))
width = 0.5

fig, ax = plt.subplots(figsize=(15, 10))
rects = ax.bar(x + width, performances, width, label="Factor")
ax.set_ylabel("Factor")
ax.set_title("Strategies Comparison")
ax.set_xticks(x, labels)
ax.legend()
ax.bar_label(rects, padding=3)
fig.tight_layout()
plt.show()
