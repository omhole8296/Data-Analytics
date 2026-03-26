## Analysis

1. Does performance differ between Fear vs Greed?

Yes, trader performance varies significantly across market sentiment conditions. Based on the analysis, both win rate and average PnL are highest during Extreme Greed, indicating that traders achieve better profitability in strongly bullish markets. In contrast, Extreme Fear shows the lowest win rate and lower PnL, suggesting that traders struggle to generate profits during highly negative sentiment. Fear and Neutral conditions show moderate performance, indicating mixed outcomes.

2. Do traders change behavior based on sentiment?

Yes, trader behavior changes noticeably with market sentiment:

Trade Frequency: Trading activity is highest during Fear, indicating increased participation during uncertain or volatile conditions.
Long/Short Bias: Traders show a slight preference for SELL positions during Fear and Greed, suggesting cautious or bearish tendencies.
Position Size: The average trade size is highest during Fear, indicating larger positions in uncertain markets, while it is lowest during Extreme Greed, suggesting more controlled risk-taking despite higher profitability.

This demonstrates that traders adjust their activity, direction, and risk exposure based on market sentiment.


Segment 1: Frequent vs Infrequent Traders

Traders were segmented based on trading activity. Frequent traders execute a higher number of trades and tend to achieve better average performance compared to infrequent traders. This suggests that active participation may improve decision-making and market timing.

Segment 2: Winners vs Losers

Traders were also segmented based on profitability. Winning traders consistently generate positive PnL, while losing traders incur losses. This highlights differences in strategy effectiveness and risk management among traders.


3 Key Insights

Trader performance is strongest during Extreme Greed, with the highest win rate and average PnL.

Traders are most active during Fear conditions, indicating that volatility drives higher trading participation.

Traders take larger positions during Fear but achieve better profitability during Extreme Greed with relatively smaller trade sizes.


## insights strategy

Strategy 1: Sentiment-Based Trade Selection

During Extreme Greed periods, traders achieve the highest win rate and profitability. Therefore, traders should prioritize trading during bullish sentiment phases and avoid excessive trading during Fear conditions, where performance is weaker. This alignment with favorable market sentiment can improve overall profitability.

Strategy 2: Dynamic Position Sizing

The analysis shows that traders take larger positions during Fear but achieve better results during Extreme Greed with smaller positions. Therefore, traders should reduce position size during Fear to manage risk and increase exposure moderately during Greed periods, where market conditions are more favorable.


## recommendations

Predictive Model Idea

A simple predictive model can be built using features such as market sentiment, trade size, trade frequency, and trade direction to predict next-day trader profitability (profit/loss classification). This can help traders anticipate favorable conditions and adjust strategies accordingly.

Clustering Idea

Traders can be clustered into different groups such as high-frequency vs low-frequency and risk-taking vs conservative traders. This helps identify which trader types perform better under different market conditions.

Dashboard Idea

A lightweight dashboard can be built using Streamlit to visualize key metrics such as PnL, win rate, and trading behavior across different market sentiment conditions. This would allow users to interactively explore patterns and gain insights for better decision-making.
