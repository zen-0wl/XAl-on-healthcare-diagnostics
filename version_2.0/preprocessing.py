import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

def preprocess_data(filepath, encoding_strategy="label", scale=True):
    """
    Preprocess the dataset with different encoding strategies.
    
    Args:
    - filepath (str): Path to the CSV file.
    - encoding_strategy (str): "label" for Label Encoding, "onehot" for One-Hot Encoding.
    - scale (bool): Whether to scale numerical features.
    
    Returns:
    - pd.DataFrame: Preprocessed feature dataframe.
    - pd.Series: Target variable.
    """
    filepath = 'healthcare-dataset-stroke-data.csv'
 
    data = pd.read_csv(filepath)

    # Drop irrelevant columns
    data = data.drop(['id'], axis=1)
    
    # Handle missing values
    data['bmi'] = data['bmi'].fillna(data['bmi'].median())
    data['smoking_status'] = data['smoking_status'].fillna('Unknown')
    
     # Add engineered features
    data["gender_stroke_risk"] = data["gender"].apply(lambda x: 1 if x.lower() == "female" else 0 if x.lower() == "male" else 0)
    data["age_stroke_risk"] = data["age"].apply(lambda x: 1 if x >= 45 else 0)
    data["hypertension_stroke_risk"] = data["hypertension"]
    data["heart_disease_stroke_risk"] = data["heart_disease"]
    data["ever_married_stroke_risk"] = data["ever_married"].apply(lambda x: 1 if x.lower() == "yes" else 0 if x.lower() == "no" else 0)
    data["work_type_stroke_risk"] = data["work_type"].apply(lambda x: 1 if x in ["Private", "Self-employed"] else 0 if x in ["Govt_job"] else 0)
    data["residence_stroke_risk"] = data["Residence_type"].apply(lambda x: 1 if x.lower() == "rural" else 0 if x.lower() == "urban" else 0)
    data["glucose_stroke_risk"] = data["avg_glucose_level"].apply(lambda x: 1 if 126 <= x <= 139.9 else 0)
    data["bmi_stroke_risk"] = data["bmi"].apply(lambda x: 1 if x < 18.5 or x >= 30 else 0)
    data["smoking_stroke_risk"] = data["smoking_status"].apply(lambda x: 1 if x.lower() == "smokes" else 0 if x.lower() == "formerly smoked" else 0)

    # Sum the risk columns to get a final risk score
    data["stroke_risk_score"] = (data[[ "gender_stroke_risk", "age_stroke_risk", "hypertension_stroke_risk",
                                        "heart_disease_stroke_risk", "ever_married_stroke_risk", "work_type_stroke_risk",
                                        "residence_stroke_risk", "glucose_stroke_risk", "bmi_stroke_risk", "smoking_stroke_risk"]]).sum(axis=1)
    
    # Apply threshold to classify stroke risk
    threshold = 3
    data["final_stroke_risk"] = data["stroke_risk_score"].apply(lambda x: 1 if x >= threshold else 0)
    
    # Separate features and target
    X = data.drop('stroke', axis=1)
    y = data['stroke']

    # Encode categorical features
    if encoding_strategy == "label":
        # Label Encoding for tree-based models
        label_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        for col in label_cols:
            X[col] = LabelEncoder().fit_transform(X[col])
    elif encoding_strategy == "onehot":
        # One-Hot Encoding for linear/distance-based models
        categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

    # Scale numerical features for linear models
    if scale:
        scaler = StandardScaler()
        X[['age', 'avg_glucose_level', 'bmi']] = scaler.fit_transform(X[['age', 'avg_glucose_level', 'bmi']])

    return X, y