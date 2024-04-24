import pandas as pd

for file in ["BTCUSDT-1m-2024-04-21.zip", "ETHUSDT-1m-2024-04-21.zip"]:
    df = pd.read_csv(f"data/raw/{file}")
    df['datetime_utc'] = pd.to_datetime(df['close_time'], unit='ms')
    df['datetime_utc_str'] = df['datetime_utc'].astype(str)
    df['time_str'] = df['datetime_utc_str'].str[11:16]
    df['pos'] = 1 # synthetic buy-and-hold strategy for app illustration

    df.to_csv(f"data/processed/{file.replace('zip', 'csv')}")
