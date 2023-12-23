

import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Function to generate a random walk
def generate_random_walk(n_steps):
    epsilon = np.random.normal(0, 1, n_steps)
    random_walk = np.cumsum(epsilon)
    return pd.Series(random_walk, name="Random Walk")

# Function to plot a time series using ggplot style
def plot_time_series(time_series, title='Time Series', xlabel='Time', ylabel='Value'):
    plt.style.use('ggplot') # Applying ggplot style
    plt.figure(figsize=(10, 6))
    plt.plot(time_series)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
