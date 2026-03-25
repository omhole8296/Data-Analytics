📌 Trader Performance vs Market Sentiment Analysis
🔹 Objective

This project analyzes the relationship between market sentiment (Fear/Greed) and trader performance using historical trading data.



🔹 Methodology
Loaded and cleaned datasets (sentiment + trader data)

Converted timestamps and aligned data by date

Merged datasets for analysis

Created key metrics:

Daily PnL per trader

Win rate

Average trade size

Trade frequency

Long/Short ratio

Visualized results using matplotlib



🔹 Key Insights
Trader performance (PnL and win rate) is highest during Extreme Greed

Trading activity is highest during Fear conditions

Traders take larger positions during Fear but achieve better profitability during Greed



🔹 Strategy Recommendations
Focus trading during Greed phases for higher profitability

Reduce position size during Fear to manage risk

Align trading strategy with market sentiment



🔹 Bonus
Proposed predictive model using sentiment + behavior features

Suggested clustering traders into behavioral groups

Proposed Streamlit dashboard for visualization



🔹 How to Run
Install required libraries:

pip install pandas matplotlib

Open the notebook:

jupyter notebook

Run all cells in the notebook
