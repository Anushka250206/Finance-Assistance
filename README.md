# 💰 WealthWise — Intelligent Financial Planning System

WealthWise is a Flask-based personal finance decision-support web app. It combines a SQLite-backed expense/asset tracker with several small ML models to give users data-driven feedback on spending, investment allocation, and retirement readiness.

> Repo name: `Finance-Assistance` — the app itself is branded **WealthWise** throughout the UI.

---

## 🚀 Features

| Module | Route | What it does |
|---|---|---|
| **Dashboard** | `/dashboard` | Central hub linking to all modules |
| **Expense & Savings Tracker** | `/expenses_savings` | Logs income vs. category-wise expenses, computes savings, stores entries in SQLite, and shows a simple AI expense forecast |
| **Expense Category Predictor (NLP)** | `/expense_category` | Classifies a free-text expense description (e.g. "Swiggy order") into a spending category using a trained NLP model, refined by a keyword-matching layer for categories like Food & Dining, Travel & Transport, Bills & Utilities, etc. |
| **Asset Growth Projection** | `/asset_growth` | Lets users add assets (type, quantity, price/unit, expected return), then projects portfolio value year-by-year using an ML pricing pipeline (with compounding fallback if the model output looks unreasonable), visualized with Chart.js |
| **Investment Pathway** | `/investment_path` | Takes age, income, savings, credit score, debt, dependents, etc., and predicts a recommended Equity/Debt/Gold/Real Estate allocation %, splits a given investment amount accordingly, and pairs it with a computed risk score |
| **Retirement Readiness** | `/retirement` | Predicts a 0–100 retirement readiness score from age, retirement age, income, expenses, savings, investment, inflation, and expected return rate, with a status label (Excellent / Good / Needs Attention) |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML:** scikit-learn-style models, serialized with `joblib` (loaded as pipelines at startup)
- **Data:** Pandas, NumPy
- **Database:** SQLite (`wealthwise.db`)
- **Frontend:** HTML5, CSS3, Bootstrap 5, Chart.js

---

## 🤖 Models & Logic

1. **Asset Growth Prediction** — `asset_pipeline` (`selected_model_pipeline.pkl`) predicts a per-unit price from price + technical-indicator-style features (RSI, MACD, moving averages, etc.), seeded with the asset's current price and rolled forward year-over-year using its expected return. `train_asset_growth_model.py` is included as a sample training script — it fits a **Decision Tree Regressor** on synthetic compound-growth data (`FV = P(1+r)^t + C·((1+r)^t−1)/r`) as a reference/fallback model.
2. **Investment Allocation** — `investment_model` takes 10 user features (age, income, savings, horizon, credit score, expenses, debt, marital status, dependents, existing investments) and outputs Equity/Debt/Gold/Real Estate percentages, normalized to sum to 100%.
3. **Risk Scoring** (`risk_engine.py`) — A rule-based engine (not ML) that combines age, savings ratio, income ratio, debt ratio, credit score, dependents, marital status, existing investments, and horizon into a single risk score, labeled `LOW` / `MODERATE` / `HIGH`.
4. **Retirement Readiness** — `retirement_linear_model_indian`, a Multiple Linear Regression model, predicts a 0–100 score (clamped) from 8 financial inputs.
5. **Expense Forecast** — A simple regression model predicts a forecasted expense figure from income alone.
6. **Expense Category NLP** — `expense_nlp_model` makes an initial prediction on the description text, then a keyword dictionary (8 categories: Food & Dining, Travel & Transport, Groceries & Essentials, Entertainment & Leisure, Health & Medical, Bills & Utilities, Education Expenses, Others) can override it for higher accuracy on common merchant/keyword patterns.
