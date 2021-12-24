# Chainge optimizer

This simulator aims to anwser to the following question: "What to do with my Chainge's rewards?" when using TF-FSN/FSN pool.
Either we keep them, waiting for the Chainge pump.
Or we can put them in USDT/CHNG pool.

Detailed simulation is in [simulation.txt](https://raw.githubusercontent.com/frossigneux/chainge-optimizer/master/output/simulation.txt).

Profit chart on 30 days, 60 days, 180 days and 365 days, depending of Chainge final price, considering a slow Chainge price increase each day:

![Profit resuts!](https://raw.githubusercontent.com/frossigneux/chainge-optimizer/master/output/figure.png "Profit")


## Chainge rewards computation

Find the APY of pools:

1. Convert APY (which may vary over time) to APR with [aprtoapy.com](https://www.aprtoapy.com/).
    - TF-FSN/FSN pool: 129% APY = 83% APR
    - USDT/CHNG pool:  430% APY = 167% APR
2. Daily rewards are applied only to USD part of the pool (or TF part in case of future pools). So if you convert 1000$ to FSN, timeframe the half, and put them in pool, it gives:
    - 1000 / 2 × 0.83 ÷ 365 = 1.14 $ / day
    - 1000 / 2 × 0.83 ÷ 365 / 0.11 = 10.34 CHNG / day (Chainge price is 0.11$)


## Impermanent loss

In future pools there is no impermament loss.
In regular USDT/CHNG pool there is impermanent loss.

We can see the impernant loss on [dailydefi.org](https://dailydefi.org/tools/impermanent-loss-calculator/).


|  CHNG $ |  Impermanent Loss % |
|---------|---------------------|
|  0.1    |  0.11               |
|  0.2    |  4.31               |
|  0.3    |  11.39              |
|  0.4    |  17.74              |
|  0.5    |  23.11              |
|  0.6    |  27.63              |
|  0.7    |  31.48              |
|  0.8    |  34.8               |
|  0.9    |  37.69              |
|  1.0    |  40.24              |
|  1.1    |  42.5               |
|  1.2    |  44.53              |
|  1.3    |  46.36              |
|  1.4    |  48.02              |
|  1.5    |  49.54              |
|  1.6    |  50.93              |
|  1.7    |  52.22              |
|  1.8    |  53.41              |
|  1.9    |  54.51              |
|  2.0    |  55.54              |


## Running

    cd chainge
    python3 chainge.py


## Installation

    sudo apt-get install python3-tk
    pip install -r requirements.txt
