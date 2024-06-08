#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"sets CLEANED.csv")


# In[11]:


print(data.head())
print(data.dtypes)


# In[12]:


# Encode categorical variables
label = preprocessing.LabelEncoder()

# Assuming 'Theme' and 'Theme_Group' are the categorical fields we want to encode
data['Theme'] = label.fit_transform(data['Theme'].astype(str))
data['Theme_Group'] = label.fit_transform(data['Theme_Group'].astype(str))

# Check for missing values and handle them (drop rows with missing values in this example)
data = data.dropna()

# Inspect the data types again
print(data.dtypes)


# In[13]:


# Select features and target variable
# Here we use 'Theme', 'Theme_Group', 'Pieces', 'Minifigures', 'Price' to predict 'Resale_Price'
features = ['Theme', 'Theme_Group', 'Pieces', 'Minifigures', 'Price']
target = 'Resale_Price'

# Create feature and target datasets
X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=200)


# In[14]:


# Build the model
reg = LinearRegression().fit(X_train, y_train)

# Predict on the test set
y_pred = reg.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# In[15]:


# Calculate correlation matrix
correlation_matrix = data.corr()

# Plot the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()


# In[ ]:




