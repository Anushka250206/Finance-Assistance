# risk_engine.py

def compute_risk_score(age, monthly_income, current_savings, investment_horizon_years,
                       credit_score, expenses_per_month, debt_amount, marital_status,
                       dependents, has_existing_investments):
    """
    Compute dynamic risk score based on inputs.
    Score: higher means more risk.
    """

    # Base score from age: Younger investors take more risk
    age_score = max(0, (100 - age) / 2)

    # Financial factors
    savings_ratio = current_savings / (monthly_income * 6)  # 6 months emergency buffer
    income_ratio = monthly_income - expenses_per_month
    debt_ratio = debt_amount / max(1, monthly_income * 12)

    savings_score = (1 - min(savings_ratio, 1)) * 30  
    income_score = (1 - min(income_ratio / monthly_income, 1)) * 20  
    debt_score = min(debt_ratio * 100, 30)  

    # Credit scores
    credit_score_adj = max(0, (800 - credit_score) / 8)

    # Social factors
    family_score = dependents * 3 + (1 if marital_status == 1 else 0) * 5

    # Existing investments reduce risk
    investment_score = -10 if has_existing_investments else 10

    # Horizon reduces risk
    horizon_score = max(0, (10 - investment_horizon_years) * 2)

    # Final score
    total_risk_score = age_score + savings_score + income_score + debt_score + credit_score_adj + family_score + investment_score + horizon_score-30

    return round(total_risk_score, 2)


def get_risk_label(risk_score):
    """
    Convert numeric score into a label.
    """
    if risk_score < 30:
        return "LOW"
    elif risk_score < 70:
        return "MODERATE"
    else:
        return "HIGH"
