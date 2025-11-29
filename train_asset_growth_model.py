# -*- coding: utf-8 -*-
"""
Train Asset Growth Prediction Model
This script trains a Decision Tree Regressor to predict future asset value
based on investment amount, annual contribution, growth rate, and years.
"""

import os
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import joblib

# -----------------------------
# 1️⃣ Generate Synthetic Dataset
# -----------------------------
np.random.seed(42)

# Features:
# [initial_investment, annual_contribution, annual_growth_rate, years]
X = np.random.uniform(low=[10000, 1000, 0.02, 1],
                      high=[1000000, 100000, 0.15, 30],
                      size=(1000, 4))

# Target: Simulate compound growth over time
# Formula ~ FV = P*(1+r)^t + C*(((1+r)^t - 1)/r)
y = []
for initial, contrib, rate, yrs in X:
    fv = initial * ((1 + rate) ** yrs) + contrib * (((1 + rate) ** yrs - 1) / rate)
    y.append(fv + np.random.uniform(-10000, 10000))  # Add slight randomness

y = np.array(y)

# -----------------------------
# 2️⃣ Train ML Model
# -----------------------------
model = DecisionTreeRegressor(max_depth=6, random_state=42)
model.fit(X, y)

# -----------------------------
# 3️⃣ Save Model Safely
# -----------------------------
import_path = os.path.dirname(os.path.abspath(__file__))            # → ...\WealthWise\backend
base_dir = os.path.dirname(import_path)                              # → ...\WealthWise
model_dir = os.path.join(base_dir, "models")                         # → ...\WealthWise\models
os.makedirs(model_dir, exist_ok=True)                                # Create folder if missing

model_path = os.path.join(model_dir, "asset_growth_model(3).pkl")

try:
    joblib.dump(model, model_path)
    print(f"✅ Model retrained and saved successfully at:\n{model_path}")
except Exception as e:
    print(f"❌ Error saving model: {e}")
