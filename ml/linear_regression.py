# PRACTICAL EXERCISE:
# Predicting Housing Prices

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'size': [650, 785, 1200, 1500, 1800],
    'price': [34500, 430000, 550000, 630000, 700000]
}

df = pd.DataFrame(data)

plt.scatter(df['size'], df['price'], color='blue')
plt.title('Housing Prices vs. Size')
plt.xlabel('Size')
plt.ylabel('Price')
plt.show()
