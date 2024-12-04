import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

file_path = 'C:/Users/zen/Documents/-- four/s2/FYP I/XAl-on-healthcare-diagnostics/version_3.0/healthcare-dataset-stroke-data.csv'
data = pd.read_csv(file_path)

print(data.info())
print(data.head())

data['bmi'] = data['bmi'].fillna(data['bmi'].mean())

data = data.drop(columns=['id'])

target_column = 'stroke'

# Separate features and target
X = data.drop(columns=[target_column])
y = data[target_column]

categorical_columns = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
numerical_columns = ['age', 'avg_glucose_level', 'bmi']

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