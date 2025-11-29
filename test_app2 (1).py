import flask
from flask import Flask, request, render_template
import joblib
import numpy as np
import os
import sqlite3

app = Flask(__name__)
DB_NAME = 'test_wealth.db'  # Using same database as expense tracker

# =================== DATABASE SETUP ===================
def init_db():
    """Creates the database tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create a table for retirement data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS retirement_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            retirement_age INTEGER,
            income REAL,
            expenses REAL,
            savings REAL,
            investment REAL,
            inflation REAL,
            return_rate REAL,
            readiness_score REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()
print("Test database 'test_wealth.db' initialized with retirement_data table.")

# =================== MODEL LOADING ===================
# Load the retirement readiness model
try:
    retirement_model = joblib.load('models/retirement_model.pkl')
    print("SUCCESS: 'models/retirement_model.pkl' loaded successfully.")
except FileNotFoundError:
    print("WARNING: 'models/retirement_model.pkl' not found. AI prediction will be disabled.")
    retirement_model = None
except Exception as e:
    print(f"Error loading retirement_model.pkl: {e}")
    retirement_model = None

# =================== FRONTEND ROUTES ===================

@app.route('/')
def index():
    # Homepage with links to both features
    return '''
        <h1>WealthWise Financial Advisor</h1>
        <p><a href="/expenses">Expense & Savings Tracker</a></p>
        <p><a href="/retirement">Retirement Readiness Analyzer</a></p>
    '''


@app.route('/retirement', methods=['GET', 'POST'])
def retirement_readiness():
    score = None
    age = None
    retirement_age = None
    income = None
    expenses = None
    savings = None
    investment = None
    inflation = None
    return_rate = None
    prediction_text = None
    recommendation = None

    if request.method == 'POST':
        try:
            # Get form data
            age = int(request.form.get('age'))
            retirement_age = int(request.form.get('retirement_age'))
            income = float(request.form.get('income'))
            expenses = float(request.form.get('expenses'))
            savings = float(request.form.get('savings'))
            investment = float(request.form.get('investment'))
            inflation = float(request.form.get('inflation'))
            return_rate = float(request.form.get('return_rate'))

            # --- 1. Get Prediction (AI Model Integration) ---
            if retirement_model:
                # Prepare features in the same order as training
                features = np.array([[age, retirement_age, income, expenses, savings, 
                                    investment, inflation, return_rate]])
                score = retirement_model.predict(features)[0]
                
                # Generate recommendation based on score
                if score >= 80:
                    recommendation = "Excellent! You're on track for a comfortable retirement."
                elif score >= 50:
                    recommendation = "Good progress! Consider increasing savings or investments."
                else:
                    recommendation = "Needs improvement. Reassess your financial strategy to boost readiness."
                
                prediction_text = f"Your AI-calculated Retirement Readiness Score: {score:.2f}%"
                print(f"SUCCESS: AI prediction generated - Score: {score:.2f}%")
            else:
                prediction_text = "AI prediction model is not loaded."
                print("INFO: AI prediction skipped (model not loaded).")

            # --- 2. SAVE to database ---
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO retirement_data 
                (age, retirement_age, income, expenses, savings, investment, inflation, return_rate, readiness_score) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (age, retirement_age, income, expenses, savings, investment, inflation, return_rate, score))
            conn.commit()
            conn.close()
            print(f"Saved to DB: Age={age}, Retirement Age={retirement_age}, Score={score}")

        except Exception as e:
            print(f"Error in /retirement POST: {e}")
            pass

    # Render the template with results
    return render_template('retirement_readiness.html',
                         score=score,
                         age=age,
                         retirement_age=retirement_age,
                         income=income,
                         expenses=expenses,
                         savings=savings,
                         investment=investment,
                         inflation=inflation,
                         return_rate=return_rate,
                         prediction_text=prediction_text,
                         recommendation=recommendation)

# =================== RUN APP ===================

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, port=5001)  # Using different port to avoid conflict