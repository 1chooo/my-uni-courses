import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import joblib
from Plum.Utils.Tools import load_data

def load_and_preprocess_data():
    df = load_data()

    # Drop irrelevant columns
    columns_to_drop = ['ObsTime', 'SeaPres', 'StnPresMaxTime', 'StnPresMinTime', 'T Max Time', 'T Min Time', 'Td dew point',
                       'RHMinTime', 'WGustTime', 'PrecpHour', 'PrecpMax10', 'PrecpMax10Time', 'PrecpMax60', 'PrecpMax60Time',
                       'SunShine', 'SunShineRate', 'GloblRad', 'VisbMean', 'EvapA', 'UVI Max', 'UVI Max Time', 'Cloud Amount']
    df.drop(columns_to_drop, axis=1, inplace=True)

    # Replace missing values
    df.replace(['...', '/'], '-999', inplace=True)
    df.replace('-999', 0.0, inplace=True)

    # Convert DataFrame to float64
    df = df.astype(np.float64)

    # Transform target column
    df['Precp'] = df['Precp'].apply(lambda x: 1 if x > 0.0 else 0)

    return df

def fill_missing_values_with_averages(df):
    observed_columns_indices = [0, 1, 2, 3, 4, 5, 8, 10]
    observation_counts = [0, 0, 0, 0, 0, 0, 0, 0]
    observation_totals = [0, 0, 0, 0, 0, 0, 0, 0]

    for row_index in range(len(df)):
        for col_index, obs_col_idx in enumerate(observed_columns_indices):
            if df.iloc[row_index, obs_col_idx] != -999.0:
                value = float(df.iloc[row_index, obs_col_idx])
                observation_counts[col_index] += 1
                observation_totals[col_index] += value

    observed_averages = [
        round(total / count, 1) if count > 0 else 0 for total, count in zip(observation_totals, observation_counts)
    ]

    stn_avg, stnmax_avg, stnmin_avg, WS_avg, WSGust_avg, T_avg, Tmax_avg, Tmin_avg = observed_averages

    columns_to_fill = [0, 1, 2, 3, 4, 5, 8, 10]
    average_values = [
        stn_avg,
        stnmax_avg,
        stnmin_avg,
        WS_avg,
        WSGust_avg,
        T_avg,
        Tmax_avg,
        Tmin_avg,
    ]

    for col_idx, avg_value in zip(columns_to_fill, average_values):
        df[df.columns[col_idx]] = df[df.columns[col_idx]].replace(-999.0, avg_value)

    return df

def fill_remaining_missing_values(df):
    columns_to_fill = [
        (6, 'RH'),
        (7, 'RHMin'),
        (9, 'WD'),
        (11, 'WDGust')
    ]

    for col_idx, col_name in columns_to_fill:
        mode_value = df[col_name].mode()[0]
        df[df.columns[col_idx]] = df[df.columns[col_idx]].replace(-999.0, mode_value)

    return df

def train_logistic_regression(df):
    X = df.drop(['Precp'], axis=1)
    y = df['Precp']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=67)
    
    lr = LogisticRegression(max_iter=200)
    lr.fit(X_train, y_train)

    predictions = lr.predict(X_test)

    return lr, X_test, y_test, predictions

def evaluate_model(lr, y_test, predictions):
    accuracy = accuracy_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    precision = precision_score(y_test, predictions)
    confusion = confusion_matrix(y_test, predictions)

    return accuracy, recall, precision, confusion

def save_model(lr, filename):
    joblib.dump(lr, filename, compress=3)

if __name__ == "__main__":
    df = load_and_preprocess_data()
    df = fill_missing_values_with_averages(df)
    df = fill_remaining_missing_values(df)
    
    lr, X_test, y_test, predictions = train_logistic_regression(df)
    
    accuracy, recall, precision, confusion = evaluate_model(lr, y_test, predictions)
    
    print("Accuracy:", accuracy)
    print("Recall:", recall)
    print("Precision:", precision)
    print("Confusion Matrix:\n", confusion)
    
    save_model(lr, 'Precipitation_Predict_2.pkl')
