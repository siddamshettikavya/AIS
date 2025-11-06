"""
Task 5 – AI in Decision-Making: Loan Approval System
====================================================
This program demonstrates:
1. A simple AI loan approval system
2. Explainability of decisions
3. Discussion of risks and fairness in AI decision-making
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')


# ============================================================================
# PART 1: GENERATE LOAN APPROVAL SYSTEM
# ============================================================================

def generate_sample_data(n_samples=500):
    """Generate synthetic loan applicant data"""
    np.random.seed(42)
    
    data = {
        'age': np.random.randint(22, 65, n_samples),
        'income': np.random.randint(20000, 150000, n_samples),
        'credit_score': np.random.randint(300, 850, n_samples),
        'loan_amount': np.random.randint(5000, 100000, n_samples),
        'employment_years': np.random.randint(0, 30, n_samples),
        'debt_to_income': np.random.uniform(0.1, 0.8, n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Create target variable (loan approval) based on simple rules
    # This simulates what a "ground truth" might look like
    df['approved'] = (
        (df['credit_score'] > 600) &
        (df['debt_to_income'] < 0.5) &
        (df['income'] > 30000) &
        (df['employment_years'] > 1)
    ).astype(int)
    
    return df


def train_black_box_model(X_train, y_train):
    """Train a complex model (Random Forest) - acts as "black box" """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def train_explainable_model(X_train, y_train):
    """Train a simple, explainable model (Logistic Regression)"""
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    return model


def explain_decision_explainable(model, applicant_data, feature_names):
    """Explain decision using model coefficients (explainable model)"""
    # Get coefficients from logistic regression
    coefficients = model.coef_[0]
    intercept = model.intercept_[0]
    
    # Calculate contribution of each feature
    contributions = {}
    for i, feature in enumerate(feature_names):
        contributions[feature] = {
            'coefficient': coefficients[i],
            'value': applicant_data[i],
            'contribution': coefficients[i] * applicant_data[i]
        }
    
    # Calculate probability
    log_odds = intercept + sum(contributions[f]['contribution'] for f in feature_names)
    probability = 1 / (1 + np.exp(-log_odds))
    
    return contributions, probability, log_odds


def explain_decision_black_box(model, applicant_data, feature_names):
    """Explain decision using feature importance (black box model)"""
    # Get feature importances
    importances = model.feature_importances_
    
    # Get prediction
    prediction = model.predict([applicant_data])[0]
    probability = model.predict_proba([applicant_data])[0][1]
    
    # Create explanation based on feature importance
    contributions = {}
    for i, feature in enumerate(feature_names):
        contributions[feature] = {
            'importance': importances[i],
            'value': applicant_data[i],
            'impact': 'High' if importances[i] > 0.2 else 'Medium' if importances[i] > 0.1 else 'Low'
        }
    
    return contributions, probability, prediction


# ============================================================================
# PART 2: ANALYZE EXPLAINABILITY
# ============================================================================

def analyze_explainability():
    """Analyze which model is more explainable"""
    print("\n" + "="*70)
    print("PART 2: EXPLAINABILITY ANALYSIS")
    print("="*70)
    
    print("\n1. EXPLAINABLE MODEL (Logistic Regression):")
    print("   ✓ Can show exact mathematical formula")
    print("   ✓ Each feature's contribution is clear (coefficients)")
    print("   ✓ Decision can be traced step-by-step")
    print("   ✓ Users can understand: 'Income increased approval by X%'")
    
    print("\n2. BLACK BOX MODEL (Random Forest):")
    print("   ✗ Complex structure with hundreds of decision trees")
    print("   ✗ Hard to explain exact decision path")
    print("   ✗ Can only show feature importance (general importance)")
    print("   ✗ Cannot explain WHY specific applicant was rejected")
    
    print("\n3. RECOMMENDATION:")
    print("   → Use explainable models for financial decisions")
    print("   → If using complex models, add explainability tools (SHAP, LIME)")
    print("   → Always provide reasons for decisions to users")


# ============================================================================
# PART 3: DISCUSSION - RISKS AND FAIRNESS
# ============================================================================

def discuss_risks_and_fairness():
    """Discuss risks of black box and importance of explainability"""
    print("\n" + "="*70)
    print("PART 3: RISKS OF BLACK BOX & FAIRNESS IN FINANCIAL DECISIONS")
    print("="*70)
    
    print("\n🚨 RISKS OF BLACK BOX AI DECISIONS:")
    print("-" * 70)
    print("1. LACK OF TRANSPARENCY:")
    print("   • Users cannot understand why their loan was rejected")
    print("   • Leads to frustration and loss of trust")
    print("   • Violates 'Right to Explanation' in GDPR regulations")
    
    print("\n2. BIAS AND DISCRIMINATION:")
    print("   • Hidden biases in training data can perpetuate discrimination")
    print("   • Model might learn unfair patterns (e.g., based on zip code)")
    print("   • Hard to detect bias without transparency")
    print("   • May discriminate against protected groups (race, gender, etc.)")
    
    print("\n3. LEGAL AND REGULATORY RISKS:")
    print("   • Financial institutions must explain credit decisions")
    print("   • Violates Equal Credit Opportunity Act (ECOA) requirements")
    print("   • Cannot defend decisions in court if challenged")
    print("   • Risk of regulatory fines and lawsuits")
    
    print("\n4. ERROR DETECTION AND CORRECTION:")
    print("   • Cannot identify when model makes mistakes")
    print("   • Difficult to debug and improve the system")
    print("   • May approve bad loans or reject good ones without reason")
    
    print("\n5. USER RELATIONSHIP:")
    print("   • Damages customer trust and satisfaction")
    print("   • Users cannot improve their profile for future applications")
    print("   • Reduces transparency in financial services")
    
    print("\n" + "="*70)
    print("✅ HOW EXPLAINABILITY ENSURES FAIRNESS:")
    print("="*70)
    
    print("\n1. TRANSPARENCY:")
    print("   • Users see exactly which factors led to the decision")
    print("   • Example: 'Your loan was rejected due to:")
    print("     - Low credit score (550 vs required 600)")
    print("     - High debt-to-income ratio (0.7 vs maximum 0.5)'")
    print("   • Users can take actionable steps to improve")
    
    print("\n2. BIAS DETECTION:")
    print("   • Can audit the model to check for unfair patterns")
    print("   • Can identify if protected attributes influence decisions")
    print("   • Allows for bias correction before deployment")
    
    print("\n3. LEGAL COMPLIANCE:")
    print("   • Meets regulatory requirements (ECOA, GDPR)")
    print("   • Can provide documented reasons for decisions")
    print("   • Defensible in legal proceedings")
    
    print("\n4. ACCOUNTABILITY:")
    print("   • Financial institutions can be held accountable")
    print("   • Errors can be identified and corrected")
    print("   • Builds trust with customers and regulators")
    
    print("\n5. FAIR TREATMENT:")
    print("   • Ensures all applicants are evaluated on same criteria")
    print("   • Prevents hidden discrimination")
    print("   • Promotes equal opportunity in financial services")
    
    print("\n6. MODEL IMPROVEMENT:")
    print("   • Can identify and fix problematic decision patterns")
    print("   • Allows continuous improvement of fairness")
    print("   • Enables human oversight and intervention")


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    print("="*70)
    print("AI LOAN APPROVAL SYSTEM WITH EXPLAINABILITY")
    print("="*70)
    
    # Generate sample data
    print("\n📊 Generating sample loan applicant data...")
    df = generate_sample_data(500)
    print(f"   Generated {len(df)} loan applications")
    print(f"   Approval rate: {df['approved'].mean()*100:.1f}%")
    
    # Prepare features
    feature_names = ['age', 'income', 'credit_score', 'loan_amount', 
                     'employment_years', 'debt_to_income']
    X = df[feature_names].values
    y = df['approved'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train models
    print("\n🤖 Training AI models...")
    black_box_model = train_black_box_model(X_train, y_train)
    explainable_model = train_explainable_model(X_train, y_train)
    
    # Evaluate models
    print("\n📈 Model Performance:")
    bb_pred = black_box_model.predict(X_test)
    exp_pred = explainable_model.predict(X_test)
    
    print(f"   Black Box (Random Forest) Accuracy: {accuracy_score(y_test, bb_pred)*100:.1f}%")
    print(f"   Explainable (Logistic Regression) Accuracy: {accuracy_score(y_test, exp_pred)*100:.1f}%")
    
    # Example: Explain a decision
    print("\n" + "="*70)
    print("EXAMPLE: EXPLAINING A LOAN DECISION")
    print("="*70)
    
    # Select a sample applicant
    sample_idx = 0
    applicant = X_test[sample_idx]
    actual_decision = y_test[sample_idx]
    
    print("\n📋 Applicant Profile:")
    for i, feature in enumerate(feature_names):
        print(f"   {feature.replace('_', ' ').title()}: {applicant[i]:.2f}")
    
    # Explain using explainable model
    print("\n" + "-"*70)
    print("EXPLAINABLE MODEL EXPLANATION:")
    print("-"*70)
    contributions, probability, log_odds = explain_decision_explainable(
        explainable_model, applicant, feature_names
    )
    
    print(f"\n   Decision: {'APPROVED' if probability > 0.5 else 'REJECTED'}")
    print(f"   Approval Probability: {probability*100:.1f}%")
    print(f"\n   Feature Contributions:")
    for feature, info in sorted(contributions.items(), 
                                key=lambda x: abs(x[1]['contribution']), 
                                reverse=True):
        sign = '+' if info['contribution'] > 0 else ''
        print(f"   • {feature.replace('_', ' ').title()}: "
              f"{sign}{info['contribution']:.4f} "
              f"(coefficient: {info['coefficient']:.4f}, value: {info['value']:.2f})")
    
    # Explain using black box model
    print("\n" + "-"*70)
    print("BLACK BOX MODEL EXPLANATION:")
    print("-"*70)
    bb_contributions, bb_probability, bb_prediction = explain_decision_black_box(
        black_box_model, applicant, feature_names
    )
    
    print(f"\n   Decision: {'APPROVED' if bb_prediction == 1 else 'REJECTED'}")
    print(f"   Approval Probability: {bb_probability*100:.1f}%")
    print(f"\n   Feature Importance (general, not specific to this applicant):")
    for feature, info in sorted(bb_contributions.items(), 
                                key=lambda x: x[1]['importance'], 
                                reverse=True):
        print(f"   • {feature.replace('_', ' ').title()}: "
              f"{info['importance']*100:.1f}% importance "
              f"(impact: {info['impact']})")
    
    print("\n" + "⚠️  NOTE: Black box model cannot explain WHY this specific")
    print("   applicant was rejected - only shows general feature importance!")
    
    # Analyze explainability
    analyze_explainability()
    
    # Discuss risks and fairness
    discuss_risks_and_fairness()
    
    print("\n" + "="*70)
    print("CONCLUSION")
    print("="*70)
    print("\n✅ Explainable AI is essential for financial decision-making")
    print("✅ Transparency builds trust and ensures fairness")
    print("✅ Always provide clear reasons for loan decisions")
    print("✅ Regular audits for bias detection are crucial")
    print("\n" + "="*70)


if __name__ == "__main__":
    main()

