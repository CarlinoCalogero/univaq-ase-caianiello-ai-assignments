import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from reader import read_csv_file_as_dictionary
import math

POSITIVE_INFINITE_PLACEHOLDER = 100000
NEGATIVE_INFINITE_PLACEHOLDER = -100000


def load_dataframe(csv_path):
    # Get the data
    data = read_csv_file_as_dictionary(csv_path)
    # Load the data into a pandas DataFrame
    df = pd.DataFrame(data)
    return df


def validate_dataframe(dataframe):
    df = dataframe.replace([math.inf], POSITIVE_INFINITE_PLACEHOLDER)  # Replace +inf with a large number
    df = df.replace([-math.inf], NEGATIVE_INFINITE_PLACEHOLDER)  # Replace -inf with a small number
    df = df.dropna()  # Drop rows with NaN values
    return df


def seishin_to_toki_no_heya(X, y, max_iter=1000, hidden_layer_sizes=(10, 5, 3), activation='relu', solver='adam',
                            random_state=42):
    # Split into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data (important for MLPs)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define and train the MLP Regressor
    mlp = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes,
                       # Hidden layers: each number before comma is number of neurons used in hidden layer
                       activation=activation,  # Activation function
                       solver=solver,  # Optimizer
                       max_iter=max_iter,  # Increase iterations for convergence
                       random_state=random_state)  # outputs training progress information during the training process.

    mlp.fit(X_train_scaled, y_train)

    print("MLP Regressor Successfully trained!")

    # Evaluate the model on the test set
    evaluate_model_on_test_set(mlp, X_test_scaled, y_test)

    return mlp, scaler


def evaluate_model_on_test_set(model, X_test_scaled, y_test):
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error on Test Set: {mse}")

    # Because dataset has significantly large or small values
    # (POSITIVE_INFINITE_PLACEHOLDER and NEGATIVE_INFINITE_PLACEHOLDER)
    # we can use another metric like Root Mean Squared Error (RMSE) for better interpretability
    rmse = mse ** 0.5
    print(f"Root Mean Squared Error: {rmse}")

    # Furthermore, to assess how significant y_pred is relative to the target range,
    # we can normalize the RMSE by the range or mean of y_test.
    # Here we have chosen to normalize it by the range
    range_of_test_set = POSITIVE_INFINITE_PLACEHOLDER - NEGATIVE_INFINITE_PLACEHOLDER
    normalized_rmse = rmse / range_of_test_set
    print(f"Normalized RMSE: {normalized_rmse * 100:.2f}%")


def train_mlp_regressor(csv_dataset_path):
    # Load DataFrame
    df = load_dataframe(csv_dataset_path)

    # Replace or drop dataframe invalid values
    df = validate_dataframe(df)

    # Split data into input (X) and target (y)
    X = df['H0'].values.reshape(-1, 1)  # Reshape to 2D array
    y = df['HL'].values  # Target

    return seishin_to_toki_no_heya(X, y)


def train_mlp_regressor_with_extended_dataset(csv_extended_dataset_path):
    # Load DataFrame
    df = load_dataframe(csv_extended_dataset_path)

    # Replace or drop dataframe invalid values
    df = validate_dataframe(df)

    # Split data into input (X) and target (y)
    X = df.drop(columns=['HL']).values
    y = df['HL'].values  # Target

    return seishin_to_toki_no_heya(X, y, 100000)
