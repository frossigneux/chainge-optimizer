# /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


invest = 1000
fsn_price = 1
chng_price = 0.11
fsn_pool = invest
fsn_pool_apr = 83  # 129
chng_pool_apr = 167  # 430

impermanent_loss = {
    0.1: 0.11,
    0.2: 4.31,
    0.1: 0.11,
    0.2: 4.31,
    0.3: 11.39,
    0.4: 17.74,
    0.5: 23.11,
    0.6: 27.63,
    0.7: 31.48,
    0.8: 34.8,
    0.9: 37.69,
    1.0: 40.24,
    1.1: 42.5,
    1.2: 44.53,
    1.3: 46.36,
    1.4: 48.02,
    1.5: 49.54,
    1.6: 50.93,
    1.7: 52.22,
    1.8: 53.41,
    1.9: 54.51,
    2.0: 55.54,
}

targets = [
    0.1,
    0.2,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    1.0,
    1.5,
    2.0,
]

performances = []
for duration in [30, 60, 180, 365]:
    for target in targets:
        total_rewards_pool_1 = 0
        total_rewards_chng_pool_2 = 0
        total_rewards_usd_pool_2 = 0
        for i in range(1, duration + 1):
            current_chng_price = chng_price + (target - chng_price) / duration * i

            print("Day", f"{i}/{duration} with final CHNG target", target)
            print("Chainge price", current_chng_price)
            print()

            # Pool FSN / TF-FSN
            underlying_usd = fsn_pool / 2
            rewards_1 = underlying_usd * fsn_pool_apr / 100 / 365 / chng_price
            print("FSN/TF-FSN pool:", fsn_pool, "FSN -", fsn_pool * fsn_price, "USD")
            print(
                "Daily rewards:",
                rewards_1,
                "CHNG -",
                rewards_1 * current_chng_price,
                "USD",
            )
            print(
                "Total rewards:",
                total_rewards_pool_1,
                "CHNG -",
                total_rewards_pool_1 * current_chng_price,
                "USD",
            )
            print()

            # Pool CHNG / USD
            rewards_2 = (
                total_rewards_chng_pool_2
                * current_chng_price
                * chng_pool_apr
                / 100
                / 365
                / current_chng_price
            )
            il_percent = impermanent_loss[int(current_chng_price * 10) / 10]
            il_chng = (
                rewards_2 * impermanent_loss[int(current_chng_price * 10) / 10] / 100
            )
            rewards_2 -= il_chng
            total_rewards_usd_pool_2 += il_chng * current_chng_price
            total_usd_rewards = (
                total_rewards_chng_pool_2 * current_chng_price
                + total_rewards_usd_pool_2
            )
            print(
                "Daily rewards:",
                rewards_2,
                "CHNG -",
                rewards_2 * current_chng_price,
                "USD",
            )
            print("Impermanent loss:", il_percent, "% -", il_chng, "CHNG")
            print(
                "USD/CHNG pool(CHNG):",
                total_rewards_chng_pool_2,
                "CHNG -",
                total_rewards_chng_pool_2 * current_chng_price,
                "USD",
            )
            print("USD/CHNG pool(USD):", total_rewards_usd_pool_2, "USD")
            print("Total rewards:", total_usd_rewards, "USD")
            print()
            total_rewards_pool_1 += rewards_1
            total_rewards_chng_pool_2 += rewards_1 + rewards_2 - il_chng

            if i == duration:
                break

        no_pool_usd = total_rewards_pool_1 * target
        factor = total_usd_rewards / no_pool_usd
        print(
            "Comparison:",
            no_pool_usd,
            "USD without secondary pool versus",
            total_usd_rewards,
            "USD with secondary pool.",
            "Strategy is",
            int(factor * 100) / 100,
            "better" if total_usd_rewards >= no_pool_usd else "worse",
            "with duration",
            duration,
            "and target",
            target,
        )
        print("###########################################")
        print()
        performances.append(total_usd_rewards / no_pool_usd)


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
