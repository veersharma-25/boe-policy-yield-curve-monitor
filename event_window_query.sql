SELECT m.event_date,m.bank_rate_before,m.bank_rate_after,m.decision_bps,m.decision_type,
p.date prior_date,p.uk_2y_yield prior_2y,p.uk_10y_yield prior_10y,
e.uk_2y_yield event_2y,e.uk_10y_yield event_10y
FROM mpc_events m
JOIN gilt_curve e ON e.date=m.event_date
JOIN gilt_curve p ON p.date=(SELECT MAX(g2.date) FROM gilt_curve g2 WHERE g2.date<m.event_date)
ORDER BY m.event_date;