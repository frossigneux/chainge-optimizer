# Chainge optimizer

This simulator aims to anwser to the following question: "What to do with my Chainge's rewards?" when using TF-FSN/FSN pool.
Either we keep them, waiting for the Chainge pump.
Or we can put them in USDT/CHNG pool.

Profit chart on 30 days, 60 days, 180 days and 365 days, depending of Chainge final price:

![Profit resuts!](https://raw.githubusercontent.com/frossigneux/chainge-optimizer/master/output/figure.png "Profit")


## Chainge rewards computation

1. Convert APY (which may vary over time) to APR with [aprtoapy.com](https://www.aprtoapy.com/).
    - TF-FSN/FSN pool: 129% APY = 83% APR
    - USDT/CHNG pool:  430% APY = 167% APR
2. Daily rewards are applied only to USD part of the pool (or TF part in case of future pools). So if you convert 1000$ to FSN, timeframe the half, and put them in pool, it gives:
    - 1000 / 2 × 0.83 ÷ 365 = 1.14 $ / day (Fusion price is 0.83$)
    - 1000 / 2 × 0.83 ÷ 365 / 0.11 = 10.34 CHNG / day (Chainge price is 0.11$)


## Impermanent loss

In future pools there is no impermament loss.
In regular USDT/CHNG pool there is impermanent loss.

We can see the impernant loss on [dailydefi.org](https://dailydefi.org/tools/impermanent-loss-calculator/).


## Running

    cd chainge
    python3 chainge.py


## Installation

    sudo apt-get install python3-tk
    pip install -r requirements.txt
