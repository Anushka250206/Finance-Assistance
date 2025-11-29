WealthWise: Intelligent Financial Planning System 📊

WealthWise is an AI-driven personal finance decision-support system designed to simplify financial planning. It combines Machine Learning with financial analytics to provide data-driven predictions, risk-aligned investment recommendations, and long-term wealth forecasts.

🚀 Key Features

📈 Asset Growth Prediction: Forecasts future values of stocks, crypto, and gold using XGBoost and Random Forest Regressors.

🧩 Smart Investment Allocation: Recommends optimal portfolio distribution (Equity, Debt, Gold, Real Estate) based on user profile and risk appetite.

👴 Retirement Readiness Score: Calculates a readiness score (0–100) using Multiple Linear Regression to assess financial preparedness for retirement.

📉 Expense & Savings Analysis: Analyzes income, expenses, and savings to provide actionable financial insights.

📊 Interactive Visualizations: Generates multi-year growth charts and portfolio gauges using Chart.js.

🛠️ Tech Stack

Language: Python

Web Framework: Flask

Machine Learning: Scikit-Learn, XGBoost

Database: SQLite

Frontend: HTML5, CSS3, Chart.js

Data Processing: Pandas, NumPy

Data Source: Yahoo Finance API (Historical Market Data)

🤖 Algorithms & Models

1. Asset Growth Prediction

Models: Random Forest Regressor & XGBoost Regressor.

Method: Trained on historical price data (AAPL, MSFT, BTC-USD, Gold Futures, etc.) with technical indicators (RSI, MACD, Moving Averages).

Performance: Achieved R² Score of ~0.92 with XGBoost.

2. Investment Allocation Model

Model: Random Forest Classifier/Regressor.

Inputs: Income, Age, Savings, Debt, Time Horizon, Risk Level.

Output: Personalized percentage allocation for various asset classes.

3. Retirement Readiness

Model: Multiple Linear Regression.

Function: Predicts a 0-100 preparedness score based on current savings rate and expected future expenses.

📂 Dataset Details

The system utilizes a hybrid data approach:

Market Data: Raw price data fetched from Yahoo Finance for 7 key tickers (S&P 500, Treasury Yields, BTC, ETH, etc.).

User Data: Stored securely in SQLite, including income, goals, and risk profiles.

Technical Indicators: Computed features like RSI-14, MACD, and Volatility to enhance prediction accuracy.

📊 Results

Accuracy: The Asset Prediction Model consistently selects XGBoost as the top performer, capturing market trends effectively.

Visuals: The dashboard provides a 50-year wealth forecast graph and a current "Retirement Readiness" gauge.

🔮 Future Scope

Live API Integration: Real-time data fetching from NSE/BSE and Crypto APIs.

Advanced Planning: Modules for specific goals like Education, Housing, and Marriage.

Deep Learning: Implementation of LSTM and Prophet models for time-series forecasting.

Mobile Support: Future development of a Flutter/React Native mobile application.

📚 References

Yahoo Finance API

Scikit-Learn Documentation

XGBoost Documentation

Investopedia (Technical Indicators)
