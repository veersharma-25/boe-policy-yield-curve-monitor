# BoE Policy & Yield Curve Monitor — SQL + Python

## Research question
How did the UK 2Y/10Y gilt curve react around Bank of England MPC decisions, and what would those moves imply for a DV01-neutral 2s10s position?

## MVP
This first version covers all 8 scheduled 2024 MPC announcements. A SQLite database stores MPC events and daily Bank of England fitted nominal 2Y/10Y curve data. SQL joins each event to the release-day and previous trading-day observations; Python calculates yield and curve changes, classifies curve moves, and models a DV01-neutral 2s10s position.

## Initial findings
- Average absolute 2Y move: 4.8bp
- Average absolute 10Y move: 4.6bp
- Average absolute 2s10s change: 3.3bp
- Largest absolute 2s10s move: 7.2bp on 2024-12-19

## Risk example
The illustrative relative-value position uses equal-and-opposite £10,000/bp DV01 legs: long 2Y and short 10Y. This is approximately first-order DV01-neutral to a parallel shift, while retaining exposure to changes in curve shape.

## Limitation
The event window is previous close to MPC-day close, not an intraday 12:00 announcement window. Other same-day news can affect yields, so results are daily event-window reactions rather than isolated causal effects.
