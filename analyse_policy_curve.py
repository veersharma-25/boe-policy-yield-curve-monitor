import sqlite3
import pandas as pd

QUERY = open("event_window_query.sql").read()
with sqlite3.connect("boe_policy_curve.db") as con:
    df = pd.read_sql_query(QUERY, con)

df["move_2y_bps"] = (df["event_2y"] - df["prior_2y"]) * 100
df["move_10y_bps"] = (df["event_10y"] - df["prior_10y"]) * 100
df["curve_change_bps"] = df["move_10y_bps"] - df["move_2y_bps"]

# DV01-neutral illustrative curve trade:
# long 2Y +£10k/bp DV01, short 10Y -£10k/bp DV01.
df["curve_trade_pnl_gbp"] = -10000*df["move_2y_bps"] + 10000*df["move_10y_bps"]
print(df)
