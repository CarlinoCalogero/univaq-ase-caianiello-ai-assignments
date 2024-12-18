import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from reader import read_csv_file_as_dictionary


def train_mlp_regressor(csv_dataset_path):
    # Get the data
    data = read_csv_file_as_dictionary(csv_dataset_path)

    # Load the data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Replace or drop invalid values
    df = df.replace([np.inf, -np.inf], np.nan)  # Replace infinities with NaN
    df = df.dropna()  # Drop rows with NaN values

    # Split data into input (X) and target (y)
    X = df['H0'].values.reshape(-1, 1)  # Reshape to 2D array
    y = df['HL'].values  # Target

    # Split into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data (important for MLPs)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define and train the MLP Regressor
    mlp = MLPRegressor(hidden_layer_sizes=(10, 5, 3),  # Three hidden layers: 10 neurons, 5 neurons and 3 neurons
                       activation='relu',  # Activation function
                       solver='adam',  # Optimizer
                       max_iter=1000,  # Increase iterations for convergence
                       random_state=42)  # outputs training progress information during the training process.

    mlp.fit(X_train_scaled, y_train)

    print("MLP Regressor Successfully trained!")

    return mlp, scaler
