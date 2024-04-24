# Trading Strategy Performance Viewer

<img src="img/banner.png" align="center" alt="" />

## Motivation

Target audience: Portfolio managers

Missed medical appointments cost the healthcare system a lot of money and affects the quality of care. If we could understand which factors lead to missed appointments it may be possible to reduce their frequency and use the saved resources to improve patient outcomes. To address this challenge, this data visualization app allows health care administrators to visually explore a dataset of missed appointments to identify potentially underlying factors, such as the day of the week, the age of the patient, and the time between scheduling and the appointment. The app shows the distribution of factors contributing to appointment show/no show and allows users to explore different aspects of this data by filtering and re-ordering on different variables in order to compare factors that contribute to absence.

## App Description

Below, we demonstrate the app's usage with toy buy-and-hold strategies based on the [BTC](https://data.binance.vision/?prefix=data/futures/um/daily/klines/BTCUSDT/1m/) and [ETH](https://data.binance.vision/?prefix=data/futures/um/daily/klines/ETHUSDT/1m/) data from Binance.

https://www.youtube.com/watch?v=t90iISeWdw8

## Installation Instructions

1. Clone this repository to your computer.

```bash
git clone https://github.ubc.ca/MDS-2023-24/DSCI_532_individual-assignment_johnshiu.git
```
```bash
cd DSCI_532_individual-assignment_johnshiu
```

2. Install the conda environment.

```bash
conda env create -f environment.yml
```

3. Activate the installed environment.

```bash
conda activate perf_viewer
```

4. Start the dashboard.

```bash
streamlit run src/app.py
```

## License

Trading Strategy Performance Viewer was created by John Shiu. It is licensed under the terms of the MIT license and the Attribution 4.0 International (CC BY 4.0 LEGAL CODE).

## Credits

Klines data in this repository is from the USDT-margined BTCUSDT and ETHUSDT futures, openly available on [Binance Market Data](https://data.binance.vision/?prefix=data/futures/um/daily/klines/).

Banner was created by [Blossom D. in CryptoStars](https://blog.cryptostars.is/whats-your-strategy-for-trading-crypto-and-stocks-99bd121b133a).
