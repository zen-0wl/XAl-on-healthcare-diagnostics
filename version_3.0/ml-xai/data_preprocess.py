import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.combine import SMOTEENN

file_path = 'C:/Users/zen/Documents/-- four/s2/FYP I/XAl-on-healthcare-diagnostics/version_3.0/healthcare-dataset-stroke-data.csv'
data = pd.read_csv(file_path)

print(data.info())
print(data.head())

data['bmi'] = data['bmi'].fillna(data['bmi'].mean())

# BMI into categorical values
def categorize_bmi(row):
    bmi = row['bmi']
    age = row['age']
    
    if pd.isnull(bmi):
        return 'Unknown'
    if age < 20:
        return 'Child'
    elif bmi <= 18.5:
        return 'Underweight'
    elif 18.5 < bmi <= 25:
        return 'Normal weight'
    elif 25 < bmi <= 30:
        return 'Overweight'
    elif bmi > 30:
        return 'Obese'
    else:
        return 'unknown'

data['bmi_category'] = data.apply(categorize_bmi, axis=1)

# Drop original numerical bmi column
data.drop(columns=['bmi'], inplace=True)

# Remove rare gender outlier
data.drop(data[data['gender'] == 'Other'].index[0], inplace=True)

# Drop unnecessary ID column
data.drop(columns=['id'], inplace=True)

data.loc[(data['smoking_status'] == 'Unknown') & (data['age'] <= 12), 'smoking_status'] = 'never smoked'

# === Map binary variables ===
data['gender'] = data['gender'].map({'Male': 1, 'Female': 0})
data['ever_married'] = data['ever_married'].map({'Yes': 1, 'No': 0})
data['Residence_type'] = data['Residence_type'].map({'Urban': 1, 'Rural': 0})

# === Normalize category strings ===
data['work_type'] = data['work_type'].map({
    'Private': 'private',
    'Self-employed': 'self_employed',
    'Govt_job': 'govt_job',
    'Never_worked': 'never_worked',
    'children': 'children'
})
data['smoking_status'] = data['smoking_status'].map({
    'formerly smoked': 'formerly_smoked',
    'never smoked': 'never_smoked',
    'Unknown': 'unknown'
})
# (bmi_category already cleaned above)

# === Define features and target ===
target_column = 'stroke'
X = data.drop(columns=[target_column])
y = data[target_column]

# === Define column types ===
categorical_columns = ['work_type', 'smoking_status', 'bmi_category']
numerical_columns = ['age', 'avg_glucose_level', 'gender', 'ever_married', 'Residence_type']

def preprocess_data(X_train, X_test, categorical_columns, numerical_columns):
    """
    Apply preprocessing pipeline to the training and testing data.

    Args:
    - X_train: The training feature data.
    - X_test: The testing feature data.
    - categorical_columns: List of categorical columns to be one-hot encoded.
    - numerical_columns: List of numerical columns to be scaled.

    Returns:
    - X_train_processed: Preprocessed training data.
    - X_test_processed: Preprocessed testing data.
    """
    # Set up a column transformer for preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_columns),  # Scale numerical columns
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)  # Encode categorical columns
        ]
    )
    

    pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

    X_train_processed = pipeline.fit_transform(X_train)
    X_test_processed = pipeline.transform(X_test)

    print(f"Processed Training Data Shape: {X_train_processed.shape}")
    print(f"Processed Testing Data Shape: {X_test_processed.shape}")
    
    return X_train_processed, X_test_processed, pipeline

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_processed, X_test_processed, pipeline = preprocess_data(X_train, X_test, categorical_columns, numerical_columns)

smote_enn = SMOTEENN(random_state=42)
X_train_resampled, y_train_resampled = smote_enn.fit_resample(X_train_processed, y_train)

# Show class distribution
print(f"Original Class Distribution:\n{y_train.value_counts()}")
print(f"Resampled Class Distribution:\n{pd.Series(y_train_resampled).value_counts()}")
print(f"Resampled Training Data Shape: {X_train_resampled.shape}")