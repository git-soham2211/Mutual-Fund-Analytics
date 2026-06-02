-- 1. Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;



-- 2. Average NAV per Month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;



-- 3. SIP YoY Growth

SELECT
year,
AVG(yoy_growth_pct) AS avg_growth
FROM monthly_sip_inflows
GROUP BY year;



-- 4. Transactions by State

SELECT
state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;



-- 5. Funds with Expense Ratio < 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;



-- 6. Highest Sharpe Ratio Funds

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;



-- 7. Highest Alpha Funds

SELECT
scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;



-- 8. Funds with Lowest Drawdown

SELECT
scheme_name,
max_drawdown_pct
FROM fact_performance
ORDER BY max_drawdown_pct ASC
LIMIT 10;



-- 9. Average Return by Category

SELECT
category,
AVG(return_3yr_pct)
FROM fact_performance
GROUP BY category;



-- 10. Top Fund Houses by AUM

SELECT
fund_house,
SUM(aum_crore)
FROM fact_performance
GROUP BY fund_house
ORDER BY SUM(aum_crore) DESC;