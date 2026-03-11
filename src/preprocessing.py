"""
Preprocessing utilities
- import precleaned data
- impute null values
- Scale data
- Encode categorical data
- Train,test,split
"""

# Imports
import numpy as np
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.config import DATA_DIR,DATA_PATH,CLEANED_DATA_Path,TEST_SIZE,TARGET_COL,RANDOM_STATE
from typing import List,Tuple

# Load precleaned data
def load_data (data_path:Path=CLEANED_DATA_Path):
    """
    load precleaned data
    remove leading and lagging white spaces 
    return clean data
    """
    
    ## Load precleaned data
    df= pd.read_csv(data_path)
    
    ## Remove leading and lagging white spaces
    df.columns =[str(c).strip() for c in df.columns.to_list()]
    return df

## Extract numerical and categorical columns
def extract_cat_col_num_cols(df:pd.DataFrame):
    """
    extracting all the categorical colums and all the numerical columns

    """
    cat_cols = df.select_dtypes(include=["object","category","bool"]).columns.to_list()
    num_cols = df.select_dtypes(include=["int64","float64","number"]).columns.to_list()
    
    return cat_cols,num_cols

## build preprocessor
def build_preprocessor (df_or_X:pd.DataFrame):
    """
    this includes input from the entire DataFrame or any feature
    """ 
    df=df_or_X.copy()
    
    # if target column is present then drop it
    if TARGET_COL in df.columns:
        df=df.drop(columns=TARGET_COL)
    else:
        df=df
    
    # Extract cat_col and num_cols
    cat_cols,num_cols =extract_cat_col_num_cols(df)
    
    # Numeric pipeline: Impute-->Scale
    num_transformer = Pipeline(steps=[
        ("imputer",SimpleImputer(strategy="median")),
       ( "scaler", StandardScaler())
    ])
    
    # categorical pipeline: Impute-->OneHotencoding
    cat_transformers = Pipeline(steps=[
        ("imputer",SimpleImputer(strategy="most_frequent")),
        ("ohe",OneHotEncoder(handle_unknown="ignore",sparse_output=False))
    ])
     
    #Combine the pipelines
    transformers =[]
    if cat_cols:
        transformers.append(("cat",cat_transformers,cat_cols))
    if num_cols:
        transformers.append(("num",num_transformer,num_cols))
    preprocessor = ColumnTransformer(transformers=transformers,remainder="drop",verbose_feature_names_out=False)
    
    return preprocessor


#Train Test and split data
def split_data(df:pd.DataFrame):
    df =df.copy()
    
    
    ## If target column is missing
    if TARGET_COL not in df.columns:
        raise KeyError(f"Target column {TARGET_COL}is not found in the DataFrame column:{df.columns.to_list()}")
    
    X=df.drop(columns=[TARGET_COL])
    y =df[TARGET_COL]
    
    X_train, X_test, y_train, y_test=train_test_split(X,y,
                                                      test_size=TEST_SIZE,
                                                      random_state=RANDOM_STATE,
                                                      stratify=y)
    return X_train,X_test,y_train,y_test


print("The preprocessing step is completed")
    
    
        

