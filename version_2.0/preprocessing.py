from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pandas as pd

# Define categorical columns
categorical_columns = [
    'gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'
]

# Preprocessing pipeline for categorical data
def label_encode_columns(df, columns):
    """
    Applies LabelEncoder to specified columns in a DataFrame.
    """
    for column in columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column].astype(str))  # Ensure all data is string to avoid errors
    return df

# Define a preprocessing pipeline
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Handle missing values
    ('labelencoder', 'passthrough')  # Placeholder to allow integration into ColumnTransformer
])

# Preprocess the data using LabelEncoder for categorical columns
def preprocess_data(df):
    # Handle missing values first
    imputer = SimpleImputer(strategy='most_frequent')
    df[categorical_columns] = imputer.fit_transform(df[categorical_columns])
    
    # Apply LabelEncoder to the categorical columns
    df = label_encode_columns(df, categorical_columns)
    return df
